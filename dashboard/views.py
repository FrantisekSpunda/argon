from django.shortcuts import render

from django.shortcuts import render
from django.contrib import messages
import dashboard

def dashboards(request):
    return render(request, 'dashboard/dashboard.html')