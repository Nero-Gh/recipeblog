from unicodedata import category
from django.contrib import admin
from .models import Category
from .models import Blog


# the class functions helps to generate slugs words from title
class adminBlog(admin.ModelAdmin):
    prepopulated_fields= {'slug': ('title',)}

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,adminBlog)
