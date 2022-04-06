from .models import News, Comments
from django.contrib import admin


class CommentsInline(admin.TabularInline):
    model = Comments


class NewsAdmin(admin.ModelAdmin):
    inlines = (CommentsInline, )
    list_display = ['id', 'title', 'created', 'updated', 'active']
    list_filter=['active']
    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, request, queryset):
        queryset.update(active=True)

    def mark_as_inactive(self, request, queryset):
        queryset.update(active=False)

    mark_as_active.short_description = 'Сделать новость активной'
    mark_as_inactive.short_description = 'Сделать новость неактивной'


class CommentsAdmin(admin.ModelAdmin):
    list_filter = ['username']
    list_display = [field.name for field in Comments._meta.get_fields()]
    actions = ['delete_by_admin']

    def delete_by_admin(self, request, queryset):
        queryset.update(text='Удалено администратором')

    delete_by_admin.short_description = 'Удалить комментарий от администратора'

admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)
