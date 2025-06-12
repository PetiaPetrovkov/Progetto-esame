from django.contrib import admin
from django.urls import path, include
from utenti import views as utenti_views

urlpatterns = [
    path('', utenti_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('utenti/', include('utenti.urls')),
    path('tornei/', include('tornei.urls')),
    path('attivita/', include('attivitasportiva.urls')),
    path('recensioni/', include('recensioni.urls')),
    path('partecipazioni/', include('partecipazioni.urls'))
]
