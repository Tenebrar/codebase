from typing import Any, Dict

from django.db.models import F
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_GET, require_http_methods

from webserver.polls.models import Choice, Question
from webserver.util.view_decorators import template_view

INDEX_SIZE = 5


@require_GET
@template_view('polls/index.html')
def index() -> Dict[str, Any]:
    questions = Question.objects.filter(publication_time__lte=timezone.now()).order_by('-publication_time')[:INDEX_SIZE]

    return {'questions': questions}


@require_http_methods(["GET", "POST"])
def detail(request: HttpRequest, *, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, publication_time__lte=timezone.now(), pk=question_id)
    context = {}

    if request.method == 'POST':
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
            selected_choice.votes = F('votes') + 1
            selected_choice.save()

            return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
        except KeyError:
            context['error_message'] = "You didn't select a choice."
        except Choice.DoesNotExist:
            context['error_message'] = 'Choice not found.'

    context.update({'question': question})
    return render(request, 'polls/detail.html', context)


@require_GET
@template_view('polls/results.html')
def results(*, question_id: int) -> Dict[str, Any]:
    question = get_object_or_404(Question, publication_time__lte=timezone.now(), pk=question_id)

    return {'question': question}
