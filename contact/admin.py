from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    

    list_display = (
        'date',
        'subject',
        'name',
        'email',
        'message',
    )

    readonly_fields = (
        'date',
    )

    ordering = ('date',)


admin.site.register(Contact, ContactAdmin)