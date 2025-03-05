from django import forms 
from .models import Forum, Comment

INPUT_CLASSES =  'py-4 px-6 rounded-xl  w-[18rem] hover:border-mustard text-lg sm:w-[20rem] md:w-[80rem] bg-black placeholder:text-white cursor:text-white border border-white'

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum 
        fields = ('title', 'content')

    title = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your title...',
    'class': INPUT_CLASSES
    }))
    
    content = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your content...',
        'class': 'text-clip overflow-hidden pt-4 pb-[40rem] px-6  rounded-xl  w-[18rem] hover:border-mustard text-lg sm:w-[20rem] md:w-[80rem] bg-black placeholder:text-white cursor:text-white border border-white'
    }))


    # use padding for inputs

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

    comment = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your comment...',
        'class': "px-6 py-4 my-4 border border-white bg-black text-white rounded-xl w-full "
    }))

    