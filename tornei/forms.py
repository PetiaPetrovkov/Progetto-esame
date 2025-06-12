from django import forms
from .models import PartecipaTorneo

class PartecipaTorneoForm(forms.ModelForm):
    class Meta:
        model = PartecipaTorneo
        fields = ['torneo']