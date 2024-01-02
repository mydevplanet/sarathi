from django.shortcuts import render
from .models import Category

# Create your views here.

def home(request):
    categories=Category.objects.all()
    print(categories)
    context={
        'categories':categories
    } 
    return render(request, 'base/index.html', context)
