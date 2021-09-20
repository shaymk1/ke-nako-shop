from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# from category.models import Category


def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products
    }
    return render(request, 'store/home.html', context)


def shop(request):
    products = Product.objects.all().filter(is_available=True)
    product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/shop.html', context)

  # #fetching products by category:
    # categories = None
    # products = None

    # if category_slug !=None:
    #   categories = get_object_or_404(Category, slug=category_slug)
    #   products = Product.objects.all().filter(is_available=True, category=categories)
    #   product_count=products.count()

    # else:
