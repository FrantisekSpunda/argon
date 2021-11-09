from django import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import Textarea
from .models import Profile

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
