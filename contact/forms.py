from django import forms 
from .models import Contact 

INPUT_CLASSES = "text-black border border-gray-400 w-4/5 px-2 placeholder:text-gray-400 py-4 rounded-xl text-left"

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your Name (or input 'Anonymous')",
        "class": INPUT_CLASSES
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': "Your Email",
        "class": INPUT_CLASSES
    }))

    subject = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your Subject (or input 'No Subject')",
        "class": INPUT_CLASSES
    }))

    message = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your Message",
        "class": INPUT_CLASSES
    }))

class AttendToForm(forms.ModelForm):
    class Meta:
        model = Contact 
        fields = ['attended_to',]

    attended_to = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        "class": "w-4 h-4 text-mustard bg-mustard border-mustard rounded focus:ring-mustard dark:focus:ring-mustard dark:ring-offset-mustard focus:ring-2 dark:bg-mustard dark:border-mustard"
    }))