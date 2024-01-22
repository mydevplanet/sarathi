from django.db import models

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