from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def example(request):
    return render(request, 'main.html')