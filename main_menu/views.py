from django.shortcuts import render
from .models import *

def draw_menu(request, menu_name):
    menu_items = MenuItem.objects.filter(url=menu_name).select_related('parent')
    return render(request, 'main_menu/base.html', {'menu_items': menu_items})

