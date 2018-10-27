from functools import wraps

from django.shortcuts import render


def template_view(template):
    def decorator(decorated_function):
        @wraps(decorated_function)
        def renderer(*args, **kwargs):
            request = args[0]
            context = decorated_function(*args[1:], **kwargs)
            return render(request, template, context)
        return renderer
    return decorator
