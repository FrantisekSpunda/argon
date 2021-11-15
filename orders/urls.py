from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('new-invoice/', views.newInvoice, name='new-invoice'),
    path('delete-invoice/<str:pk>/', views.deleteInvoice, name='delete-invoice'),
    path('invoice/<str:pk>/', views.invoice, name='invoice'),
    path('invoices/', views.invoices, name='invoices'),
    path('new-client/', views.newClient, name='new-client'),
    path('delete-client/<str:pk>', views.deleteClient, name='delete-client'),
    path('client/<str:pk>', views.client, name='client'),
    path('clients/', views.clients, name='clients'),

    path('pdf-invoice/<str:pk>', views.pdfInvoice, name='pdf-invoice'),
]