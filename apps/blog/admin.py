from django.contrib import admin
from apps.blog.models import Blog, Category, Comment

admin.site.register(Blog)
admin.site.register(Category)
# 5 added Comments for management in Django Admin
admin.site.register(Comment)