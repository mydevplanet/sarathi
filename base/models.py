from django.db import models
import os
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    vol_heading=models.TextField()
    vol_content=models.TextField()
    vol_image=models.ImageField(upload_to='volunteer/')

    class Meta:
        verbose_name_plural='volunteers'
    def __str__(self):
        return self.vol_heading
    
class Slide(models.Model):
    slide_image=models.ImageField(upload_to='slide')
    slide_heading=models.CharField(max_length=100)
    slide_content=models.CharField(max_length=200)
    slide_is_active=models.BooleanField(default=False)
    class Meta:
        verbose_name_plural='slides'
    def __str__(self):
        return self.slide_heading
    
def upload_to(instance, filename):
    folder_name=f"post_{instance.id}"
    return os.path.join('blog_images', folder_name, filename)


class Blog(models.Model):
    blog_title=models.CharField(max_length=200)
    blog_image=models.ImageField(upload_to=upload_to)
    content_with_images = RichTextField()
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})

    def __str__(self):
        return self.blog_title

class Testimonial(models.Model):
    testimonial_message=models.TextField()
    testimonial_title=models.CharField(max_length=100)
    testimonial_image=models.ImageField(upload_to='testimonial/')

    def __str__(self):
        return self.testimonial_title