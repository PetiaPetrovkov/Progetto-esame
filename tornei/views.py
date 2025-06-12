from django.shortcuts import render, redirect
from .forms import PartecipaTorneoForm

def partecipa_torneo(request):
    messaggio = None  # Qui memorizziamo il messaggio di conferma
    if request.method == 'POST':
        form = PartecipaTorneoForm(request.POST)
        if form.is_valid():
            partecipazione = form.save(commit=False)
            partecipazione.sportivo = request.user.sportivo
            try:
                partecipazione.save()
                messaggio = f"Hai partecipato con successo al torneo: {partecipazione.torneo.nome_torneo}!"
                form = PartecipaTorneoForm()  # Pulisce il form dopo l'invio
            except ValueError as e:
                form.add_error(None, str(e))
    else:
        form = PartecipaTorneoForm()
    return render(request, 'tornei/partecipa.html', {'form': form, 'messaggio': messaggio})
