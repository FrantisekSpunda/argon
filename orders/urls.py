from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('new-invoice/', views.newInvoice, name='new-invoice')
]