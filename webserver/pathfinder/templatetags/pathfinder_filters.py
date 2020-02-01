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


@register.filter
def exact_length(unknown_length_list, desired_length):
    unknown_length_list = list(unknown_length_list or [])  # copy

    # pad the list with as many empty strings as needed
    unknown_length_list += ([''] * (desired_length - len(unknown_length_list)))  # 0 or negative values cause no change

    return unknown_length_list[:desired_length]


@register.filter
def times(number):
    return range(number)

