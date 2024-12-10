from django import forms
from .models import FlashcardSet, Flashcard

class FlashcardSetForm(forms.ModelForm):
    class Meta:
        model = FlashcardSet
        fields = ['title', 'description']

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['flashcard_set', 'question', 'answer', 'hidden'] 
