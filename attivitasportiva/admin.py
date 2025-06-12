from django.contrib import admin
from .models import AttivitaSportiva, PartecipaAttivita

@admin.register(AttivitaSportiva)
class AttivitaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'giorno_settimana', 'orario', 'istruttore']
    list_filter = ['giorno_settimana']
    search_fields = ['nome']

@admin.register(PartecipaAttivita)
class PartecipaAttivitaAdmin(admin.ModelAdmin):
    list_display = ['sportivo', 'attivita']
    list_filter = ['attivita']
