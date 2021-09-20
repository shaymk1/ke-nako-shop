from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from store.models import Product

# fetching products by category:


def fetching_products_by_category(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            is_available=True, category=categories)
        product_count = products.count()

    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {

        'products': products,
        'product_count': product_count
    }

    return render(request, 'category/category.html', context)
