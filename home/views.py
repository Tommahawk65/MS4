from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product, Category



def index(request):
    """ A view to return the index page """

    featured_product_1 = get_object_or_404(Product, sku=1)
    featured_product_2 = get_object_or_404(Product, sku=3)
    featured_product_3 = get_object_or_404(Product, sku=5)
    featured_product_4 = get_object_or_404(Product, sku=9)
    featured_product_5 = get_object_or_404(Product, sku=11)
    featured_product_6 = get_object_or_404(Product, sku=15)
    featured_product_7 = get_object_or_404(Product, sku=17)
    featured_product_8 = get_object_or_404(Product, sku=19)
    featured_product_9 = get_object_or_404(Product, sku=21)
    featured_product_10 = get_object_or_404(Product, sku=23)
    featured_product_11 = get_object_or_404(Product, sku=25)
    featured_product_12 = get_object_or_404(Product, sku=27)
    

    context = {
        'featured_product_1': featured_product_1,
        'featured_product_2': featured_product_2,
        'featured_product_3': featured_product_3,
        'featured_product_4': featured_product_4,
        'featured_product_5': featured_product_5,
        'featured_product_6': featured_product_6,
        'featured_product_7': featured_product_7,
        'featured_product_8': featured_product_8,
        'featured_product_9': featured_product_9,
        'featured_product_10': featured_product_10,
        'featured_product_11': featured_product_11,
        'featured_product_12': featured_product_12,
    }
    return render(request, 'home/index.html', context)
    

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)