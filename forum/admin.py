from django.contrib import admin

from .models import Forum, Comment


class ForumAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'created_at', 'modified_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['forum', 'comment', 'author']

admin.site.register(Forum, ForumAdmin)
admin.site.register(Comment, CommentAdmin)