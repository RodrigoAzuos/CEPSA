from django.urls import path,include
from core import views

urlpatterns = [
    path('cursos/', views.RegistrarCursoViews.as_view() , name = 'cursos'),
    path('alunos/', views.RegistrarAlunoView.as_view() , name = 'alunos'),
    path('turmas/', views.RegistrarTurmaViews.as_view() , name = 'turmas'),
    path('disciplinas/', views.RegistrarDisciplinaViews.as_view() , name = 'disciplinas'),
]
