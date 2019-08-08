from functools import wraps
from typing import Any, Callable, Dict, List

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import resolve, reverse
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST

from webserver.polls.models import Choice, Question
from webserver.util.view_decorators import template_view

INDEX_SIZE = 5


@require_GET
@template_view('polls/index.html')
def index() -> Dict[str, Any]:
    questions = Question.objects.filter(publication_time__lte=timezone.now()).order_by('-publication_time')[:INDEX_SIZE]

    return {'questions': questions}


@require_GET
@template_view('polls/detail.html')
def detail(*, question_id: int) -> Dict[str, Any]:
    question = get_object_or_404(Question, publication_time__lte=timezone.now(), pk=question_id)

    return {'question': question}


@require_GET
@template_view('polls/results.html')
def results(*, question_id: int) -> Dict[str, Any]:
    question = get_object_or_404(Question, publication_time__lte=timezone.now(), pk=question_id)

    return {'question': question}


@require_POST
def vote(request: HttpRequest, *, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, publication_time__lte=timezone.now(), pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

        selected_choice.votes = F('votes') + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    except KeyError as e:
        request.error_message = f"You didn't select a {e.args[0]}."
    except ObjectDoesNotExist as e:
        request.error_message = f"{str(type(e)).split('.')[-2]} not found."

    request.method = 'GET'
    view = resolve(reverse('polls:detail', args=(question_id,))).func
    return view(request, question_id=question_id)

    # request.method = 'GET'
    # return detail(request, question_id=question_id)

    # return render(request, 'polls/detail.html', {
    #     'question': question,
    #     'request': request
    # })


# SANDBOX

def post_view(required_args: List[str], success: str, fail: Callable[..., HttpResponse]):
    def decorator(decorated_function: Callable[..., bool]) -> Callable[..., HttpResponse]:
        @wraps(decorated_function)
        def renderer(*args: HttpRequest, **kwargs: Any) -> HttpResponse:
            request, = args

            try:
                additional_kwargs = {required_arg: request.POST[required_arg] for required_arg in required_args}
            except KeyError:
                result = False
                error_message = ''
            else:
                result = decorated_function(*args, **{**kwargs, **additional_kwargs})

            if result:
                return HttpResponseRedirect(reverse(success, args=kwargs.keys()))
            else:
                # No need to redirect, because it will reload at the same url
                return render(request, fail, {
                    'question': question,
                    'error_message': error_message,
                })
        return renderer
    return decorator


@require_POST
@post_view(required_args=['choice'], success='polls:results', fail='polls:detail')
def vote2(*, question_id: int, choice: str) -> bool:
    question = get_object_or_404(Question, publication_time__lte=timezone.now(), pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=choice)
    except Choice.DoesNotExist:
        return False

    selected_choice.votes = F('votes') + 1
    selected_choice.save()

    return True

