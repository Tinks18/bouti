from django.contrib import admin
from .models import Post, Response, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_responses']

    def approve_responses(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('title', 'product_name', 'content', 'rating')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)
