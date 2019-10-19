from django import forms
from webapp.models import Poll, Choice, Answer


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ['created_at']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text', 'poll']


class ChoiceForPollForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ['poll']


class AnswerForPollForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['poll']


