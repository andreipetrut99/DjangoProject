from django import forms
from django.forms import TextInput

from notes.models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text']

        widgets = {
            'title': TextInput(attrs={'placeholder': 'Name of note', 'class': 'form-control'}),
            'text': TextInput(attrs={'placeholder': 'Text of note', 'class': 'form-control'})
        }