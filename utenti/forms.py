from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utente, Sportivo, Istruttore

class UtenteForm(UserCreationForm):
    class Meta:
        model = Utente
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'tipo_utente']

class SportivoForm(forms.ModelForm):
    class Meta:
        model = Sportivo
        fields = ['preferenze_sportive']

class IstruttoreForm(forms.ModelForm):
    class Meta:
        model = Istruttore
        fields = ['competenze', 'disponibilita']
