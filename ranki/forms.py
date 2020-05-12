from django import forms
from .models import Card, Deck


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['question', 'answer', 'deck', 'image']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'rows': '4'}),
            'answer': forms.TextInput(attrs={'class': 'form-control', 'rows': '4'}),
            'deck': forms.Select(attrs={'class': 'form-control', 'empty_label': 'None'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
