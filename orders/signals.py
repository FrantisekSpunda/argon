from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Invoice

from django.core.mail import send_mail
from django.conf import settings



def sendInvoice(sender, instance, created, **kwargs):
    invoice = instance

    if invoice.sended == True:

        subject = 'Invoice numb.: '+ invoice.invoice_id +' from '+ invoice.supplier.first_name +' '+ invoice.supplier.last_name
        message = 'Sended invoice from argon web.'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [invoice.client.client_email],
            fail_silently=False,
        )

post_save.connect(sendInvoice, sender=Invoice)