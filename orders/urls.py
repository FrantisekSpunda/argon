from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('new-invoice/', views.newInvoice, name='new-invoice'),
    path('invoice/<str:pk>/', views.invoice, name='invoice'),
    path('invoices/', views.invoices, name='invoices'),
    path('clients/', views.clients, name='clients'),
]