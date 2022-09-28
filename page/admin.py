from django.contrib import admin

# Register your models here.
from .models import Author, Blog, BlogTag

admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(BlogTag)

