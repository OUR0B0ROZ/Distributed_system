from django.db import models
from django.utils.text import slugify
import random
from .code_generator import generate_code
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title

class ModelTest(models.Model):
    autor = models.ForeignKey(User,
        related_name='models_created',
        on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
        related_name='models',
        on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    code_1=models.CharField(max_length=10,unique=True)
   
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.title
   
