from django import template

register = template.Library()

@register.filter(name="percentage")
def multiply(value):
    return round(value * 100, 3)