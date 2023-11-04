from django import template
from main_menu.models import MenuItem
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(url=menu_name).select_related('parent')
    return mark_safe(render_menu(menu_items))

def render_menu(menu):
    result = '<ul>'
    for item in menu:
        result += '<li>'
        result += '<a href="' + item.url + '">' + item.title + '</a>'
        if item.children.exists():
            result += render_menu(item.children.all())
        result += '</li>'
    result += '</ul>'
    return result