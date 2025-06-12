from .models import Recensione
from .forms import RecensioneForm
from django.utils import timezone
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

def scrivi_recensione(request):
    if request.method == 'POST':
        form = RecensioneForm(request.POST)
        if form.is_valid():
            recensione = form.save(commit=False)
            recensione.sportivo = request.user.sportivo  # automaticamente lo sportivo loggato
            recensione.data_recensione = timezone.now()  # imposta data a oggi
            recensione.save()
            return redirect('dashboard')
    else:
        form = RecensioneForm()
    return render(request, 'recensioni/scrivi.html', {'form': form})
def lista_recensioni(request):
    recensioni = Recensione.objects.select_related('sportivo', 'attivita').all()
    return render(request, 'recensioni/lista_recensioni.html', {'recensioni': recensioni})

def cancella_recensione(request, id):
    recensione = get_object_or_404(Recensione, id=id, sportivo=request.user.sportivo)
    recensione.delete()
    return redirect('lista_recensioni')