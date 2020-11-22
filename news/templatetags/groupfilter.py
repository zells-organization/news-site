from django import template

register = template.Library()


@register.filter(name='group')
def group(u, group_names):
    return u.groups.filter(name=group_names)
