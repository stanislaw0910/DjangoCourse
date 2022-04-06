from django.contrib import admin
from . models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'price']


admin.site.register(Item, ItemAdmin)
