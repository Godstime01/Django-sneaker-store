from django import template

register = template.Library()

@register.simple_tag
def multiply(value1, value2):
    return value1 * value2


@register.simple_tag
def add(value1, value2):
    return value1 + value2
