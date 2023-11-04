from django.urls import path
from main_menu.views import *

urlpatterns = [
    path('<slug:menu_name>/', draw_menu, name='draw_menu'),

]