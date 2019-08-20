from functools import wraps
from logging import getLogger
from typing import Any, Callable, Dict

from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
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
            return render(request, template_name, context)
        return renderer
    return decorator


def required_get_parameters(*required_args: str, logging_function: Callable[[str], Any]=logger.warning) ->\
        Callable[[Callable[..., HttpResponse]], Callable[..., HttpResponse]]:
    """
    :param required_args: The GET parameters required to be present for the GET call to work
    :param logging_function: A function taking error messages in case something is missing
    :return:
    """
    def decorator(decorated_function: Callable[..., HttpResponse]) -> Callable[..., HttpResponse]:
        """
        Decorator that will have a view return 'Bad request' if some required GET parameters are missing.
        :param decorated_function: A function that returns an HttpResponse
        :return: The same function prefixed with the check for required parameters (and returning a 400 if needed)
        """
        @wraps(decorated_function)
        def wrapper(*args: HttpRequest, **kwargs: Any) -> HttpResponse:
            """
            :param args: The positional arguments for the view (should only be the HttpRequest)
            :param kwargs: The keyword arguments for the view
            :return: The HttpResponse of the view if all needed parameters are present; a 400 response otherwise
            """
            request, = args

            for required_arg in required_args:
                required = request.GET.get(required_arg)
                if not required:
                    logging_function(f'No {required_arg} in call to {decorated_function} with parameters {request.GET}')
                    return HttpResponseBadRequest()  # 400

            additional_kwargs = {required_arg: request.GET[required_arg] for required_arg in required_args}
            return decorated_function(*args, **{**kwargs, **additional_kwargs})
        return wrapper
    return decorator
