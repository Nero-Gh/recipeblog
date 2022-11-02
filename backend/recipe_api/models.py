from random import choices
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Blog(models.Model):
    POST_CHOICES = [
        ('POPULAR', 'Popular')
    ]
    category = models.ForeignKey(Category,on_delete=models.CASCADE ,null=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    excerpt = models.CharField(max_length = 255, default='')
    content = models.TextField(null=True,blank=True)
    ContentTwo = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    incredients = models.TextField(null=True,blank=True)
    postlabel = models.CharField(max_length=100, choices=POST_CHOICES , null = True, blank=True)

    def __str__(self):
        return self.title