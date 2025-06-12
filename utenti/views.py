from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UtenteForm, SportivoForm, IstruttoreForm
from .models import Utente, Sportivo, Istruttore
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UtenteForm, SportivoForm, IstruttoreForm
from .models import Utente, Sportivo, Istruttore
from django.http import HttpResponseForbidden

def registrazione_sportivo(request):
    if request.method == 'POST':
        form_utente = UtenteForm(request.POST)
        form_sportivo = SportivoForm(request.POST)
        if form_utente.is_valid() and form_sportivo.is_valid():
            utente = form_utente.save(commit=False)
            utente.tipo_utente = 'sportivo'
            utente.save()
            sportivo = form_sportivo.save(commit=False)
            sportivo.utente = utente
            sportivo.save()
            return redirect('login')
    else:
        form_utente = UtenteForm()
        form_sportivo = SportivoForm()
    return render(request, 'utenti/registrazione_sportivo.html', {
        'form_utente': form_utente,
        'form_sportivo': form_sportivo,
    })

def registrazione_istruttore(request):
    if request.method == 'POST':
        form_utente = UtenteForm(request.POST)
        form_istruttore = IstruttoreForm(request.POST)
        if form_utente.is_valid() and form_istruttore.is_valid():
            utente = form_utente.save(commit=False)
            utente.tipo_utente = 'istruttore'
            utente.save()
            istruttore = form_istruttore.save(commit=False)
            istruttore.utente = utente
            istruttore.save()
            return redirect('login')
    else:
        form_utente = UtenteForm()
        form_istruttore = IstruttoreForm()
    return render(request, 'utenti/registrazione_istruttore.html', {
        'form_utente': form_utente,
        'form_istruttore': form_istruttore,
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'utenti/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    utente = request.user

    if utente.tipo_utente == 'sportivo':
        return render(request, 'utenti/dashboard.html', {'utente': utente})
    elif utente.tipo_utente == 'istruttore':
        return render(request, 'utenti/dashboard_istruttore.html', {'utente': utente})
    elif utente.tipo_utente == 'gestore':
        return render(request, 'utenti/dashboard_gestore.html', {'utente': utente})
    else:
        return HttpResponseForbidden("Non hai accesso a questa sezione.")

def home(request):
    return render(request, 'home.html')
