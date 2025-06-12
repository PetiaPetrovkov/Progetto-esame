from django.shortcuts import render, redirect
from .forms import PartecipaAttivitaForm

def partecipa_attivita(request):
    messaggio = None
    if request.method == 'POST':
        form = PartecipaAttivitaForm(request.POST)
        if form.is_valid():
            partecipazione = form.save(commit=False)
            partecipazione.sportivo = request.user.sportivo
            try:
                partecipazione.save()
                messaggio = f"Hai partecipato con successo all'attività: {partecipazione.attivita.nome}!"
                form = PartecipaAttivitaForm()  # resetta il form
            except ValueError as e:
                form.add_error(None, str(e))
    else:
        form = PartecipaAttivitaForm()
    return render(request, 'attivitasportiva/partecipa.html', {'form': form, 'messaggio': messaggio})
