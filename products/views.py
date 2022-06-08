from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category



def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
   

    
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
    else:
        user = None

