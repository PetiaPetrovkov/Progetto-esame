from django.db import models
from utenti.models import Sportivo
from utenti.models import Utente  # Per GestoreTorneo

class GestoreTorneo(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Torneo(models.Model):
    nome_torneo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    data_inizio = models.DateField()
    data_fine = models.DateField()
    max_partecipanti = models.IntegerField()
    gestore = models.ForeignKey(GestoreTorneo, on_delete=models.CASCADE, related_name='tornei')

    def __str__(self):
        return self.nome_torneo

class PartecipaTorneo(models.Model):
    sportivo = models.ForeignKey(Sportivo, on_delete=models.CASCADE)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if PartecipaTorneo.objects.filter(torneo=self.torneo).count() >= self.torneo.max_partecipanti:
            raise ValueError("Limite massimo di partecipanti raggiunto per questo torneo.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sportivo} partecipa a {self.torneo}"
