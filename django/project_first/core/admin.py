from django.contrib import admin
from django.utils import timezone
import datetime
from .models import Profile, Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.unregister(User)

admin.site.register(Profile)


# admin.site.register(Post)
# admin.site.register(Comment)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    max_num = 3


def delete_old_posts(modeladmin, request, queryset):
    queryset.filter(date_pub__lte=timezone.now() - datetime.timedelta(weeks=3)).delete()  # lte - меньше чем


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # fields = ['author', 'description', 'image', 'get_likes']
    readonly_fields = ['get_likes']
    fieldsets = [
        ('Main', {
            'fields': ['author', 'image', 'description']
        }),
        ('info', {
            'fields': ['get_likes']
        })
    ]
    inlines = [CommentInline]
    list_display = ('author', 'date_pub', 'get_likes')
    list_filter = ('author', )
    actions = [delete_old_posts]


class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = [ProfileInline]
