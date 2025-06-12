from django.contrib import admin
from .models import Utente, Sportivo, Istruttore
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = Utente
    fieldsets = UserAdmin.fieldsets + (
        ('Tipo Utente', {'fields': ('tipo_utente',)}),
    )
    list_display = ['username', 'first_name', 'last_name', 'email', 'tipo_utente']
    list_filter = ['tipo_utente']
    search_fields = ['username', 'email']

admin.site.register(Utente, CustomUserAdmin)

@admin.register(Sportivo)
class SportivoAdmin(admin.ModelAdmin):
    list_display = ['utente', 'preferenze_sportive']
    search_fields = ['utente__username']

@admin.register(Istruttore)
class IstruttoreAdmin(admin.ModelAdmin):
    list_display = ['utente', 'competenze']
    search_fields = ['utente__username']
