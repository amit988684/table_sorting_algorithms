from django import template

from django_tables2.templatetags.django_tables2 import querystring

register = template.Library()

@register.inclusion_tag('django_tables2/header.html', takes_context=True)
def render_header(context):
    for column in context['table'].columns:
        column.sort_existing = False
        if 'sort' in context['request'].GET:
            if column.name in context['request'].GET['sort']:
                column.sort_existing = True

    return context