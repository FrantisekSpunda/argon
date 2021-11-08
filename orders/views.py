from django.shortcuts import redirect, render
from django.contrib import messages

def frontpage(request):
    return redirect('dashboard')

def dashboard(request):
    return render(request, 'orders/dashboard.html')