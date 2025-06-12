from django.db import models
from utenti.models import Istruttore, Sportivo

class AttivitaSportiva(models.Model):
    nome = models.CharField(max_length=100)
    orario = models.TimeField()
    giorno_settimana = models.CharField(max_length=15)
    max_partecipanti = models.IntegerField()
    istruttore = models.ForeignKey(Istruttore, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class PartecipaAttivita(models.Model):
    sportivo = models.ForeignKey(Sportivo, on_delete=models.CASCADE)
    attivita = models.ForeignKey(AttivitaSportiva, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if PartecipaAttivita.objects.filter(attivita=self.attivita).count() >= self.attivita.max_partecipanti:
            raise ValueError("Limite massimo di partecipanti raggiunto per questa attività.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sportivo} partecipa a {self.attivita}"
