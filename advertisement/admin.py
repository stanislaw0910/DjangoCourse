from django.contrib import admin
from .models import Advertisement, Author, AdvertisementType


class AdvertisementAdmin(admin.ModelAdmin):
    search_fields = ['description']


class AdvertTypeAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    fields = (('name', 'phone_number'), 'email')
    list_display = ['name', 'phone_number']
    list_filter = ['name']


admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(AdvertisementType, AdvertTypeAdmin)
admin.site.register(Author, AuthorAdmin)
