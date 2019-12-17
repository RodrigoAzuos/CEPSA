from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from django.views.generic.base import View
from usuarios.views import  MyView, get_usuario_logado
from aula.forms import AulaForm

# Create your views here.
from aula.models import Aula

class RegistrarAulaView(MyView,View ):
    def get(self, request):
        form = AulaForm()
        return render(request, 'aula.html', {'form':form})

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
        # aula =
        form = AulaForm()
        return render(request, 'aula.html', {'form':form})

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
