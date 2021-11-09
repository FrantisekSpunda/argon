from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.editProfile, name='profile'),

    path('logout/', views.logoutUser, name='logout'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
]