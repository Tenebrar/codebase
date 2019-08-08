from functools import wraps
from logging import getLogger
from typing import Any, Callable, Dict

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

logger = getLogger(__name__)


def template_view(template_name: str) -> Callable[[Callable[..., Dict[str, Any]]], Callable[..., HttpResponse]]:
    """
    :param template_name: The name of a template to use
    :return: A decorator (see docs below)
    """
    def decorator(decorated_function: Callable[..., Dict[str, Any]]) -> Callable[..., HttpResponse]:
        """
        :param decorated_function: A function that returns a context
        :return: A function that returns a HttpResponse using that context with the decorated template
        """
        @wraps(decorated_function)
        def renderer(*args: HttpRequest, **kwargs: Any) -> HttpResponse:
            """
            :param args: The positional arguments for the view (should only be the HttpRequest)
            :param kwargs: The keyword arguments for the view
            :return: An HttpResponse that is a rendered template with a context determined by the wrapped function
            """
            request, = args
            context = decorated_function(**kwargs)
            context.update({'request': request})
            return render(request, template_name, context)
        return renderer
    return decorator


def required_get_parameters(*required_args, log_function=logger.warning):
    """Decorator that will have a view return 'Bad request' if some required GET parameters are missing."""
    def decorator(decorated_function):
        @wraps(decorated_function)
        def wrapper(*args, **kwargs):
            request = args[0]

            for required_arg in required_args:
                required = request.GET.get(required_arg)
                if not required:  # Not present or empty string
                    log_function(f'No {required_arg} in call to {decorated_function} with parameters {request.GET}')
                    return HttpResponse(status=400)  # Bad request

            additional_kwargs = {required_arg: request.GET[required_arg] for required_arg in required_args}
            return decorated_function(*args, **{**kwargs, **additional_kwargs})
        return wrapper
    return decorator
