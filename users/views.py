from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def profileEdit(request):
    profile = request.user.profile

    context = {'profile': profile}
    return render(request, 'users/profile.html', context)