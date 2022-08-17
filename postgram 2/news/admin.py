from django.contrib import admin
import datetime

from .models import AdvUser, Post, Comment



class PostAdmin(admin.ModelAdmin):
    list_display = ('id','content', 'author', 'pubdate','image','file','video','audio')
    list_display_links = ('content',)
    search_fields = ('content', 'author','image','file','video','audio')
    date_hierarchy = 'pubdate'
    fields = ('author','content','image','file','video','audio')

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'pubdate','post','image','file','video','audio')
    date_hierarchy = 'pubdate'
    fields = ('author','content','post','image','file','video','audio')

admin.site.register(Comment, CommentAdmin)

class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username','avatar', 'email', 'first_name', 'last_name')
    fields = (('username','email','avatar'), ('first_name', 'last_name'),
              ('is_active', 'is_activated'), ('is_staff', 'is_superuser'),
              'groups', 'user_permissions', ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')

admin.site.register(AdvUser, AdvUserAdmin)