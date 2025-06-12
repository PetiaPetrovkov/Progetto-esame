from django.urls import path
from . import views

urlpatterns = [
    path('registrazione_sportivo/', views.registrazione_sportivo, name='registrazione_sportivo'),
    path('registrazione_istruttore/', views.registrazione_istruttore, name='registrazione_istruttore'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
