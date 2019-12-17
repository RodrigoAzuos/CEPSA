from django.urls import path,include
from django.contrib.auth.views import login, logout_then_login
from aula import views

urlpatterns = [
    ##Usuario##
    path('registrar-aula/', views.RegistrarAulaView.as_view() , name = 'cadastrar_aula'),
    path('aula/<int:aula_id>/', views.AulaView.as_view() , name = 'aula'),
]
