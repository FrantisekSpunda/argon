from django.shortcuts import render
from django.contrib import messages

from users.models import Profile
from .forms import ProfileForm

# Create your views here.
def profileEdit(request):
    profile = request.user.profile

    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

    context = {'profile': profile, 'form': form}
    return render(request, 'users/profile.html', context)