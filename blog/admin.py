from django.contrib import admin
from .models import Blog,Category, Post, Comment
from django.utils.safestring import mark_safe

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","slug",)
    list_editable = ("is_active", "is_home",)
    search_fields = ("title","description",)
    readonly_fields = ("slug",)
    list_filter = ("is_active","is_home","categories",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
