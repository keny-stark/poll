from django import forms
from webapp.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll

        widgets = {
            'text': forms.TextInput,
        }
        exclude = ['created_at']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        widgets = {
            'text': forms.TextInput,
        }
        fields = ['text', 'poll']

