from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name', 
            'email', 
            'subject',
            'message', 
            )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['subject'].widget.attrs['placeholder'] = False
        for field in self.fields:
            if field != 'subject':
                placeholder = f'{placeholders[field]} *'
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False