from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from MS4.decorators import authenticate_product, authenticate_review

from products.models import Product
from .models import ProductReview

from .forms import ProductReviewForm


@login_required
@authenticate_product
def add_product_review(request, product_id):

    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.product = product
            review.save()
            messages.success(request, 'Successfully added product review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add review. \
                                     Please ensure the form is valid.')
    else:
        form = ProductReviewForm()

    template = 'reviews/add_product_review.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)


@login_required
@authenticate_product
@authenticate_review
def edit_product_review(request, product_id, review_id):
    """ Add a review and rating to the product """

    product = Product.objects.get(pk=product_id)
    review = ProductReview.objects.get(pk=review_id)

    if request.method == 'POST':
        form = ProductReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.product = product
            review.save()
            messages.success(request,
                                'Successfully updated product review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed update review. \
                                        Please ensure the form is valid.')
    else:
        form = ProductReviewForm(instance=review)

    template = 'reviews/edit_product_review.html'
    context = {
        'form': form,
        'product': product,
        'review': review
    }

    return render(request, template, context)


@login_required
@authenticate_product
@authenticate_review
def delete_product_review(request, product_id, review_id):
    """
    Deletes user's review
    """
    product = Product.objects.get(pk=product_id)
    review = ProductReview.objects.get(pk=review_id)

    try:
        review.delete()

        messages.success(request, 'Successfully deleted product review!')

    # If deletion failed, return an error message
    except Exception as e:
        messages.error(request, "We couldn't delete your review because "
                                f" eroor:{e} occured. Try again later.")

    return redirect(reverse('product_detail', args=(review.product.id,)))