from django.contrib import admin

# Register your models here.
 
from .models import MenuItem, Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'parent')
    prepopulated_fields = {'slug': ('name',)}


