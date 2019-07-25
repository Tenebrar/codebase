from typing import Any, Dict

from django.db.models import F
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from webserver.util.view_decorators import template_view
from .models import Choice, Question

INDEX_SIZE = 5


@template_view('polls/index.html')
def index() -> Dict[str, Any]:
    questions = Question.objects.order_by('-publication_date')[:INDEX_SIZE]

    return {'questions': questions}


@template_view('polls/detail.html')
def detail(*, question_id: int) -> Dict[str, Any]:
    question = get_object_or_404(Question, pk=question_id)

    return {'question': question}


@template_view('polls/results.html')
def results(*, question_id: int) -> Dict[str, Any]:
    question = get_object_or_404(Question, pk=question_id)

    return {'question': question}


def vote(request: HttpRequest, *, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    selected_choice.votes = F('votes') + 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
