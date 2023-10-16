from django.contrib import admin
from .models import Category, ModelTest
# Register your models here.
@admin.register(Category)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(ModelTest)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created','code']
    list_filter = ['created', 'category']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
