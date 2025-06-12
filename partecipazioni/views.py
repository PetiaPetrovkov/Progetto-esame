from django.shortcuts import render, redirect, get_object_or_404
from attivitasportiva.models import PartecipaAttivita
from tornei.models import PartecipaTorneo

def mie_partecipazioni(request):
    sportivo = request.user.sportivo
    attivita = PartecipaAttivita.objects.filter(sportivo=sportivo)
    tornei = PartecipaTorneo.objects.filter(sportivo=sportivo)
    return render(request, 'partecipazioni/lista.html', {
        'attivita': attivita,
        'tornei': tornei
    })

def cancella_attivita(request, id):
    partecipazione = get_object_or_404(PartecipaAttivita, id=id, sportivo=request.user.sportivo)
    partecipazione.delete()
    return redirect('mie_partecipazioni')

def cancella_torneo(request, id):
    partecipazione = get_object_or_404(PartecipaTorneo, id=id, sportivo=request.user.sportivo)
    partecipazione.delete()
    return redirect('mie_partecipazioni')
