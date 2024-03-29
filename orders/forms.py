from django import forms
from django.contrib.auth import models
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Client, Invoice, Item

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ['supplier']
    
    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control', 'placeholder': name.replace('_', ' ').capitalize()})

        self.fields['date_exposure'].widget.attrs.update({'type': 'date'})
        self.fields['date_maturity'].widget.attrs.update({'type': 'date'})

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': name.replace('_', ' ')})

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': name.replace('_', ' ').capitalize()})