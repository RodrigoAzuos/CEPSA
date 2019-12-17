from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from django.views.generic.base import View
from usuarios.views import  MyView, get_usuario_logado
from aula.forms import AulaForm, OcorrenciaForm

# Create your views here.
from aula.models import Aula, Ocorrencia
from core.models import Aluno

class RegistrarAulaView(MyView,View ):
    def get(self, request):
        form = AulaForm()
        aulas = Aula.objects.all()
        return render(request, 'index.html', {'form':form, 'aulas': aulas})

    def post(self, request):
        form = AulaForm(request.POST, request.FILES)

        if (form.is_valid()):
            dados = form.data
            try:
                material = request.FILES['material']
            except:
                material = None

            try:
                aula = Aula(data=dados['data'],
                                aulas_ministradas=dados['aulas_ministradas'],
                                assunto=dados['assunto'],
                                descricao=dados['descricao'],
                                material=material)


                aula.save()
                print('salvou')
                return redirect('index')

            except(ValidationError):
                form.adiciona_erro("Digite uma data no formato YYYY-mm-dd")

        print(form.data)
        return render(request, 'index.html', {'form': form})


class AulaView(MyView,View):
    def get(self, request, aula_id):
        aula = Aula.objects.get(pk=aula_id)
        form = OcorrenciaForm()
        alunos = Aluno.objects.all()
        return render(request, 'aula.html', {'form':form, 'aula':aula, 'alunos':alunos})

    def post(self, request, aula_id):
        form = OcorrenciaForm(request.POST)
        aula = Aula.objects.get(pk=aula_id)

        if (form.is_valid()):
            dados = form.data
            ocorrencia = Ocorrencia(
                titulo=dados['titulo'],
                descricao=dados['descricao'],
                aula=aula)

            ocorrencia.save()

            return redirect('aula', aula_id)

        return render(request, 'aula.html', {'form': form, 'aula': aula})
