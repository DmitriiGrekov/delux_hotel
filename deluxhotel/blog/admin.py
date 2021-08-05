from django.contrib import admin
from .models import TagsModel, BlogPostModel, CommentModel


@admin.register(TagsModel)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BlogPostModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'author',
                    'publish_date',
                    'active')
    list_display_links = ('title', 'author')
    search_fields = ('title', 'author', 'text',)
    list_filter = ('author', 'publish_date', 'tags')
    prepopulated_fields = {'slug': ('title', 'author',)}


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'email',
                    'date_publish')
    list_display_links = ('name',
                          'email')
    search_fields = ('name',
                     'email')
    list_filter = ('date_publish',
                   'post')
