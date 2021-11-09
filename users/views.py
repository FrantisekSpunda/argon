from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.contrib.auth.models import User
from users.models import Profile
from .forms import ProfileForm, CustomUserCreationForm

@login_required(login_url='login')
def editProfile(request):
    profile = request.user.profile

    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

    context = {'profile': profile, 'form': form}
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist.')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password is incorret.')
    return render(request, 'users/login.html')

def registerUser(request):
    form = CustomUserCreationForm()

    if request.user.is_authenticated:
        return redirect('dashboard')


    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            print(user)
            user.save()
                       
            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('profile')
        
        else: 
            messages.error(request, 'An error has occured during registration.')

    context = {'form':form}
    return render(request, 'users/register.html', context)