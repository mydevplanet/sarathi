from django.shortcuts import render
from .models import Category, Volunteer, Slide

# Create your views here.

def home(request):
    categories=Category.objects.all()
    volunteer=Volunteer.objects.first()
    slides=Slide.objects.all()
    # print(categories)
    context={
        'categories':categories,
        'volunteer':volunteer,
        'slides':slides
    } 
    return render(request, 'base/index.html', context)
