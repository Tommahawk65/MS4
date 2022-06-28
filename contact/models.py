from django.db import models


SUBJECT_MENU = (
    ('general_query', 'GENERAL QUERY'),
    ('account_issue', 'ACCOUNT ISSUE'),
    ('product_enquiry', 'PRODUCT ENQUIRY'),
    ('order', 'ORDER'),
    ('refund_request', 'REFUND REQUEST'),
)


class Contact(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False)
    subject = models.CharField(max_length=100, choices=SUBJECT_MENU,
                               default='general_query',
                               null=False, blank=False)
    message = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name