from django.shortcuts import render
from .models import *

# def draw_menu(request, menu_name):
#     menu_items= MenuItem.objects.all()
#     menu = render_menu(menu_items)
#     return render(request, 'main_menu/menu.html', {'menu': menu})
#
# def render_menu(menu):
#     result = '<ul>'
#     for item in menu:
#         result += '<li>'
#         result += '<a href="' + item.url + '">' + item.title + '</a>'
#         if item.children.exists():
#             result += render_menu(item.children.all())
#         result += '</li>'
#     result += '</ul>'
#     return result
def draw_menu(request, menu_name):
    menu_items = MenuItem.objects.filter(url=menu_name).select_related('parent')
    #(menu_name)
    return render(request, 'main_menu/menu.html', {'menu_items': menu_items})