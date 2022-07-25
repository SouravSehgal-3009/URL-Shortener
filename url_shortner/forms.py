from .models import ShortURL
from django import forms

class CreateNewShortURL(forms.ModelForm):
    class Meta:
        model=ShortURL
        fields = {'longurl'}

        widgets = {
            'longurl': forms.TextInput(attrs={'class': 'form-control'})
        }

