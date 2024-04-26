from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {}
    context['products']=products
    return render(request,'index.html',context)

def product_detail(request):

    products = Product.objects.filter
    context = {}
    context['products']=products
    return render(request, 'product_detail.html',context)


    

