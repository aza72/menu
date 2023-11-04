from django.contrib import admin
from .models import *




class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent')
    list_filter = ('title',)
    search_fields = ('title', 'url')
    ordering = ('title',)
    save_on_top = True

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.site_title = 'Админ-панель редактирования меню'
admin.site.site_header = 'Админ-панель редактирования меню'