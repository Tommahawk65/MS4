from django import forms

from .models import ProductReview



RATING_CHOICES = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))


class ProductReviewForm(forms.ModelForm):
    class Meta:

        model = ProductReview
        fields = ('rating',
                  'title',
                  'review')

        widgets = {
            'rating': forms.Select(choices=RATING_CHOICES)
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        super(ProductReviewForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'text-white'