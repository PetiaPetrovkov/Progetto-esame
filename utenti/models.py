from django.contrib.auth.models import AbstractUser
from django.db import models

class Utente(AbstractUser):
    TIPO_UTENTE = (
        ('sportivo', 'Sportivo'),
        ('istruttore', 'Istruttore'),
        ('gestore', 'Gestore'),
    )
    tipo_utente = models.CharField(max_length=10, choices=TIPO_UTENTE, default='sportivo')

    def __str__(self):
        return f"{self.username} ({self.tipo_utente})"

class Sportivo(models.Model):
    utente = models.OneToOneField(Utente, on_delete=models.CASCADE)
    preferenze_sportive = models.TextField()

    def __str__(self):
        return str(self.utente)

class Istruttore(models.Model):
    utente = models.OneToOneField(Utente, on_delete=models.CASCADE)
    competenze = models.TextField()
    disponibilita = models.TextField()

    def __str__(self):
        return str(self.utente)
