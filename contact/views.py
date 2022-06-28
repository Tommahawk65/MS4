from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm


def contact(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was submitted successfully. \
                We will be in touch soon')
            
            instance = form.save()

            sender_email = instance.email
            subject = render_to_string(
                'contact/contact_emails/contact_email_subject.txt',
                {'instance': instance})
            body = render_to_string(
                'contact/contact_emails/contact_email_body.txt',
                {'instance': instance,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                subject,
                body, settings.DEFAULT_FROM_EMAIL,
                [sender_email]
            )
        else:
            messages.error(
                request, 'There was a problem with the form. \
                Please try again')
        return redirect(reverse('home'))

    form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
        'on_contact_page': True
    }

    return render(request, template, context)
