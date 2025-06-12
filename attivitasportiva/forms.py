from django import forms
from .models import PartecipaAttivita

class PartecipaAttivitaForm(forms.ModelForm):
    class Meta:
        model = PartecipaAttivita
        fields = ['attivita']
