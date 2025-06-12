from django.db import models
from utenti.models import Sportivo
from attivitasportiva.models import AttivitaSportiva

class Recensione(models.Model):
    sportivo = models.ForeignKey(Sportivo, on_delete=models.CASCADE)
    attivita = models.ForeignKey(AttivitaSportiva, on_delete=models.CASCADE)
    testo = models.TextField()
    data_recensione = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Recensione di {self.sportivo} per {self.attivita}"
