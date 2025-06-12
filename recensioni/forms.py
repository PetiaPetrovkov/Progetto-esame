from django import forms
from .models import Recensione

class RecensioneForm(forms.ModelForm):
    class Meta:
        model = Recensione
        exclude = ['sportivo', 'data_recensione']  # Esclude dal form perché lo gestisci da views
