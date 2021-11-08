from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, 'sales/dashboard.html')