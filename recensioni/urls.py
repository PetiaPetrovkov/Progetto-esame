from django.urls import path
from . import views

urlpatterns = [
    path('scrivi/', views.scrivi_recensione, name='scrivi_recensione'),
    path('tutte/', views.lista_recensioni, name='lista_recensioni'),
    path('cancella/<int:id>/', views.cancella_recensione, name='cancella_recensione'),

]
