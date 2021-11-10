from django.contrib import messages
from django.db.models.base import ModelStateFieldsCacheDescriptor
from datetime import datetime, timedelta
from django.db import models
from users.models import Profile
import uuid

class Invoice(models.Model):
    invoice_id = models.CharField(blank=True, max_length=8, null=True, unique=True)
    supplier = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    
    subscriber_name = models.CharField(max_length=128, null=True, blank=True)
    subscriber_ic = models.CharField(max_length=128, null=True, blank=True)
    subscriber_dic = models.CharField(max_length=128, null=True, blank=True)
    subscriber_email = models.EmailField(max_length=128, blank=True, null=True)
    subscriber_address = models.CharField(max_length=128, blank=True, null=True)
    subscriber_city = models.CharField(max_length=64, blank=True, null=True)
    subscriber_country = models.CharField(max_length=128, blank=True, null=True)
    subscriber_postal_code = models.CharField(max_length=5, blank=True, null=True)

    date_expiration = models.DateField(default=datetime.now())
    date_maturity = models.DateField(default=datetime.now()+timedelta(days=30))

    total_price = models.FloatField(default=0, null=True, blank=True)

    account_number = models.CharField(max_length=128, blank=True)
    variable_symbol = models.CharField(max_length=128, blank=True)

    text = models.TextField(max_length=256, default='Put some text here for subscriber...')

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.invoice_id

    @property
    def getTotalPrice(self):
        items = self.items_all.all().filter(value=self.invoice_id).count()
        
        for item in items:
            self.total_price += item.price

        self.save()

class Item(models.Model):
    invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    price = models.FloatField(default=0, blank=True)
    dph = models.FloatField(default=21, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name