from django import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control', 'type': 'text'})

        for key in self.fields:
            self.fields[key].required = True

        self.fields['first_name'].widget.attrs.update({'placeholder':'First name'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'Last name'})
        self.fields['username'].widget.attrs.update({'placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email', 'type': 'email'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password', 'type': 'password'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Repeat password', 'type': 'password'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user'] 

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control', 'placeholder': name, 'type': 'text'})

        self.fields['username'].widget.attrs.update({'id': 'input-username'})
        self.fields['email'].widget.attrs.update({'id': 'input-email', 'type': 'email'})
        self.fields['first_name'].widget.attrs.update({'id': 'input-first-name'})
        self.fields['last_name'].widget.attrs.update({'id': 'input-last-name'})
        self.fields['about_me'].widget.attrs.update({'rows': '4', 'placeholder': 'A few words about you ...'})