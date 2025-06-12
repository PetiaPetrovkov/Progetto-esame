from django.urls import path
from . import views

urlpatterns = [
    path('partecipa/', views.partecipa_attivita, name='partecipa_attivita'),
]
