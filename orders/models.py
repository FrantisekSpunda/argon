from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.db import models
from users.models import Profile
import uuid

class Order(models.Model):
    order_id = models.CharField(blank=True, max_length=8)
    supplier = models.CharField(max_length=128, null=True, blank=True)
    supplier_address = models.CharField(max_length=128)
    subscriber = models.CharField(max_length=128, null=True, blank=True)
    subscriber_address = models.CharField(max_length=128)
    total_price = models.FloatField(default=0, null=True, blank=True)

    account_number = models.CharField(max_length=128, blank=True)
    variable_symbol = models.CharField(max_length=128, blank=True)

    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.order_id

    @property
    def getTotalPrice(self):
        items = self.items_all.all().filter(value=self.order_id).count()
        
        for item in items:
            self.total_price += item.price

        self.save()

class Item(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    price = models.FloatField(default=0, blank=True)
    dph = models.FloatField(default=21, blank=True)
    
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name