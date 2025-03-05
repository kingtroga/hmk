from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Profile

INPUT_CLASSES =  'py-4 px-6 rounded-xl  w-[18rem] hover:border-mustard text-lg sm:w-[20rem] md:w-[80rem] bg-black placeholder:text-white cursor:text-white border border-white'

class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    first_name = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your title...',
    'class': INPUT_CLASSES
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your content...',
        'class': INPUT_CLASSES
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your title...',
    'class': INPUT_CLASSES
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your content...',
        'class': INPUT_CLASSES
    }))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']


    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'placeholder': 'Your content...',
        'class': INPUT_CLASSES
    }))

