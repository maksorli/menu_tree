from django.contrib import admin

# Register your models here.

# menu_app/admin.py

from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_name', 'parent')
    list_filter = ('menu_name',)
    search_fields = ('name',)

admin.site.register(MenuItem, MenuItemAdmin)
