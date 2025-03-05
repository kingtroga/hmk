from django import forms
from .models import Blog

INPUT_CLASSES =  'py-4 px-6 rounded-xl  w-[18rem] hover:border-mustard text-lg sm:w-[20rem] md:w-[80rem] bg-black placeholder:text-white cursor:text-white border border-white'


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('image', 'title', 'content')




    title = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your title...',
    'class': INPUT_CLASSES
    }))

    content = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your content...',
        'class': 'text-clip overflow-hidden pt-4 pb-[40rem] px-6  rounded-xl  w-[18rem] hover:border-mustard text-lg sm:w-[20rem] md:w-[80rem] bg-black placeholder:text-white cursor:text-white border border-white'
    }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': INPUT_CLASSES #'text-clip overflow-hidden pt-4 pb-[40rem] px-6  rounded-xl  w-[18rem] hover:border-mustard text-lg sm:w-[20rem] md:w-[80rem] bg-black placeholder:text-white cursor:text-white border border-white'
    }))

