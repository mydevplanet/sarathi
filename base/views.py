from django.shortcuts import render
from .models import Category, Volunteer, Slide, Blog

# Create your views here.

def home(request):
    categories=Category.objects.all()
    volunteer=Volunteer.objects.first()
    slides=Slide.objects.all()
    blogs=Blog.objects.all()
    # print(categories)
    context={
        'categories':categories,
        'volunteer':volunteer,
        'slides':slides,
        'blogs':blogs,
    } 
    return render(request, 'base/index.html', context)
