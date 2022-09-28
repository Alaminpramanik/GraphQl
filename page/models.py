from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField() 

class Blog(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, verbose_name=('author'), related_name='blog',
                                    on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField()  


class BlogTag(models.Model):
    blog = models.ForeignKey(Blog, verbose_name=('blog'), related_name='blog_tags',
                                    on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.CharField(max_length=250) 