from functools import wraps
from typing import Any, Callable, Dict

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


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
