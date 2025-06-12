from django.urls import path
from . import views

urlpatterns = [
    path('', views.mie_partecipazioni, name='mie_partecipazioni'),
    path('cancella-attivita/<int:id>/', views.cancella_attivita, name='cancella_attivita'),
    path('cancella-torneo/<int:id>/', views.cancella_torneo, name='cancella_torneo'),
]
