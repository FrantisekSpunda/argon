from django.contrib import messages
from django.db.models.base import ModelStateFieldsCacheDescriptor
from datetime import datetime, timedelta
from django.db import models
from users.models import Profile
import uuid

class Invoice(models.Model):
    invoice_id = models.CharField(blank=True, max_length=8, null=True, unique=True)
    supplier = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    
    subscriber_name = models.CharField(max_length=128, null=True)
    subscriber_ic = models.CharField(max_length=128, null=True)
    subscriber_dic = models.CharField(max_length=128, null=True)
    subscriber_email = models.EmailField(max_length=128, null=True)
    subscriber_address = models.CharField(max_length=128, null=True)
    subscriber_city = models.CharField(max_length=64, null=True)
    subscriber_country = models.CharField(max_length=128, null=True)
    subscriber_postal_code = models.CharField(max_length=5, null=True)

    date_exposure = models.DateField(default=datetime.now())
    date_maturity = models.DateField(default=datetime.now()+timedelta(days=30))

    total_price = models.FloatField(default=0, null=True, blank=True)

    account_number = models.CharField(max_length=128)
    variable_symbol = models.CharField(max_length=128)

    text = models.TextField(max_length=256, default='Put some text here for subscriber...')

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.invoice_id

    @property
    def getTotalPrice(self):
        items = self.item_set.all()
        
        for item in items:
            self.total_price += (item.price * item.amouth)

        self.save()

class Item(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=128, null=True)
    price = models.FloatField(default=0, null=True, blank=True)
    amouth = models.IntegerField(default=1, null=True, blank=True)
    dph = models.FloatField(default=21, null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    item_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.invoice.invoice_id) + ' - ' + str(self.name)