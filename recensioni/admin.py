from django.contrib import admin
from .models import Recensione

@admin.register(Recensione)
class RecensioneAdmin(admin.ModelAdmin):
    list_display = ['sportivo', 'attivita', 'data_recensione']
    list_filter = ['data_recensione']
    search_fields = ['testo']
