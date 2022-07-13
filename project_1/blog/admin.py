from django.contrib import admin
from .models import Post, Tag, Comment, Product

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Product)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)