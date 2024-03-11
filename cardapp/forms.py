from django import forms
from.models import Card

class MovieForm(forms.ModelForm):
    class Meta:
        model=Card
        fields=['name','description','year','image']