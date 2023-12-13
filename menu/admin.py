from django.contrib import admin

# Register your models here.
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent')  # Добавляем 'url' в список отображаемых полей
    prepopulated_fields = {'url': ('title',)}

admin.site.register(MenuItem, MenuItemAdmin)