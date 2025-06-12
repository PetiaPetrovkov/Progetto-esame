from django.urls import path
from . import views

urlpatterns = [
    path('partecipa/', views.partecipa_torneo, name='partecipa_torneo'),
]
