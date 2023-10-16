from django.db import models
from django.utils.text import slugify
from .code_generator import generate_code  # Import the generate_code function
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
    code = models.CharField(max_length=10, unique=True)  # Add a field to store the generated code
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.code:  # Generate code only if it's not already set
            generated_code = generate_code()  # Use the external code generation function
            self.code = generated_code

        # Generate a unique slug based on the title
        if not self.slug:
            self.slug = slugify(self.title)

        super(ModelTest, self).save(*args, **kwargs)