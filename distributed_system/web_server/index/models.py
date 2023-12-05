from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title


def generate_slug(title):
    return slugify(title)

class ModelTest(models.Model):
    autor = models.ForeignKey(User,
                              related_name='models_created',
                              on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
                                 related_name='models',
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    creation_year = models.PositiveIntegerField()  # Field for storing the year of creation
    initial = models.CharField(max_length=1)  # Field for storing the first letter of the title

    class Meta:
        ordering = ['initial', '-creation_year', 'title']

    def save(self, *args, **kwargs):
        # Generate slug, set creation_year, and initial before saving
        if not self.slug:
            self.slug = generate_slug(self.title)
        self.creation_year = self.created.year
        self.initial = self.title[0].upper()  # Store the first letter (capitalized)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title