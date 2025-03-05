from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': "Type your message here",
                'class': 'bg-black text-white border border-white w-full h-[4rem] py-4 px-6 rounded-xl border'
            })
        }