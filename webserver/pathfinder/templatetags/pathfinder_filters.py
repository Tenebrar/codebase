from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
@stringfilter
def or_space(value):
    return value or mark_safe('&nbsp;')


@register.filter
@stringfilter
def or_slash(value):
    return value or '/'


@register.filter
def or_zero(value):
    return value or 0
