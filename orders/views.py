from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def frontpage(request):
    return redirect('dashboard')

@login_required(login_url='login')
def dashboard(request):
    profile = request.user.profile

    context = {'profile': profile}
    return render(request, 'orders/dashboard.html', context)