from django.shortcuts import render
from mainapp.models import Product


def index(request):
    context = {
        'products': Product.objects.all()[:4]
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    sub_links = [
        {'href': 'products_all', 'title': 'все'},
        {'href': 'products_home', 'title': 'дом'},
        {'href': 'products_office', 'title': 'офис'},
        {'href': 'products_modern', 'title': 'модерн'},
        {'href': 'products_classic', 'title': 'классика'},
    ]

    context = {
        'sub_links': sub_links
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')
