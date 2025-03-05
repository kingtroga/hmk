from django import forms
from django.contrib.auth.models import User
from hmk.accounts.models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

INPUT_CLASSES =  'py-4 px-6 rounded-xl  w-[18rem] hover:border-mustard text-lg sm:w-[20rem] md:w-[30rem] bg-black placeholder:text-white cursor:text-white border border-white'

class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your username',
    'class': INPUT_CLASSES
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': INPUT_CLASSES
    }))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    first_name = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your first name',
    'class': INPUT_CLASSES
    }))


    last_name = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your last name',
    'class': INPUT_CLASSES
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your username',
    'class': INPUT_CLASSES
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': INPUT_CLASSES
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': INPUT_CLASSES
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': INPUT_CLASSES
    }))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

    avatar = forms.CharField(widget=forms.FileInput(attrs={
        'class': INPUT_CLASSES #'text-clip overflow-hidden pt-4 pb-[40rem] px-6  rounded-xl  w-[18rem] hover:border-mustard text-lg sm:w-[20rem] md:w-[80rem] bg-black placeholder:text-white cursor:text-white border border-white'
    }))


