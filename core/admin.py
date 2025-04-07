from django.contrib import admin
from .models import PostModel, CategoryModel, Comment
# Register your models here.

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    ordering = ['-id']


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'author',
        'created_at',
        'is_published',
    ]
    ordering = ['-id']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post']