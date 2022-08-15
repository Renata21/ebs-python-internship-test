from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 1 - added boolean field for Blog model and added this field in blog_blog table 
    enabled = models.BooleanField(default=True)


class Comment(models.Model):
    '''
    4 added Comment model to save comments for each blog post 
    '''
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
