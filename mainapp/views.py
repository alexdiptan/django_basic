from django.shortcuts import render
from mainapp.models import Product, Category


def index(request):
    context = {
        'products': Product.objects.all()[:4]
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'sub_links': Category.objects.all()
    }
    return render(request, 'mainapp/products.html', context)


def products_list(request, pk):
    print(pk)
    context = {
        'sub_links': Category.objects.all()
    }
    return render(request, 'mainapp/products.html', context)

def contact(request):
    return render(request, 'mainapp/contact.html')
