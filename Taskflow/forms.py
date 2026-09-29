from django import forms
from .models import Taches

class TachesForm(forms.ModelForm):
    class Meta:
        model = Taches
        fields = '__all__'
        widgets = {
        'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        } 
