from django.contrib import admin
from .models import Torneo, PartecipaTorneo, GestoreTorneo

@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
    list_display = ['nome_torneo', 'tipo', 'data_inizio', 'max_partecipanti']
    list_filter = ['tipo']
    search_fields = ['nome_torneo']

@admin.register(GestoreTorneo)
class GestoreAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email']
    search_fields = ['nome', 'email']

@admin.register(PartecipaTorneo)
class PartecipaTorneoAdmin(admin.ModelAdmin):
    list_display = ['sportivo', 'torneo']
    list_filter = ['torneo']
