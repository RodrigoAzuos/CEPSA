from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from usuarios.views import  MyView, get_usuario_logado
from aula.forms import AulaForm
from core.forms import CursoForm, RegistraAlunoForm, TurmaForm, DisciplinaForm
from core.models import Curso, Aluno, Turma, Disciplina
from aula.models import Aula

# Create your views here.


def index(request):
    form = AulaForm()
    aulas = Aula.objects.all()

    return render(request, 'index.html',{'form':form, 'aulas': aulas})

class RegistrarCursoViews(MyView, View):

    def get(self, request):
        form = CursoForm()
        cursos = Curso.objects.all()

        return render(request,"cursos.html",{'form':form, 'cursos':cursos})

    def post(self, request):
        form = CursoForm(request.POST)

        if (form.is_valid()):
            dados = form.data

            curso = Curso(nome=dados['nome'],
                            descricao=dados['descricao']
                          )

            curso.save()

            return redirect('cursos')

        return render(request, 'cursos.html', {'form': form})


class RegistrarAlunoView(MyView, View):
    def get(self, request):

        alunos = Aluno.objects.all()
        logado = get_usuario_logado(request)

        if not logado.is_superuser:
            return render(request,'permissao.html')

        form = RegistraAlunoForm()
        return render(request, 'registrar_aluno.html', {'form': form, 'alunos': alunos, 'logado': logado})

    def post(self, request):
        form = RegistraAlunoForm(request.POST)
        alunos = Aluno.objects.all()

        if not get_usuario_logado(request).is_superuser:
            return render(request,'permissao.html')

        if (form.is_valid()):
            dados = form.data

            aluno = Aluno(nome=dados['nome'],
                 data_nascimento=dados['data_nascimento'],
                 telefone=dados['telefone'],
                 sexo=dados['sexo'],
                 )

            aluno.save()
            mensagem = 'Aluno cadastrado. Nome:  %s' %(dados['nome'])
            logado = get_usuario_logado(request)

            return render(request, 'registrar_aluno.html', {'form': form, 'mensagem': mensagem, 'alunos': alunos, 'logado': logado })

        return render(request, 'registrar_aluno.html', {'form': form, 'alunos': alunos})

class RegistrarTurmaViews(MyView,View):

    def get(self, request):
        form = TurmaForm()
        turmas = Turma.objects.all()
        return render(request,"turmas.html",{'form':form, 'turmas':turmas})

    def post(self, request):
        form = TurmaForm(request.POST)
        turmas = Turma.objects.all()

        if (form.is_valid()):
            dados = form.data

            curso = Curso.objects.get(pk = dados['curso'])
            ministrante = User.objects.get(pk=dados['ministrante'])
            disciplina = Disciplina.objects.get(pk=dados['disciplina'])

            print(dados)
            turma = Turma(ministrante=ministrante,
                        curso=curso,
                        disciplina=disciplina,
                        carga_horaria=dados['carga_horaria'],
                          )

            turma.save()

            return redirect('turmas')

        return render(request, 'turmas.html', {'form': form, 'turmas':turmas})

class RegistrarDisciplinaViews(MyView, View):

    def get(self, request):
        form = DisciplinaForm()
        disciplinas = Disciplina.objects.all()

        return render(request,"disciplinas.html",{'form':form, 'disciplinas':disciplinas})

    def post(self, request):
        form = DisciplinaForm(request.POST)
        disciplinas = Disciplina.objects.all()

        if (form.is_valid()):
            dados = form.data
            disciplina = Disciplina(nome=dados['nome'],
                            descricao=dados['descricao']
                          )

            disciplina.save()

            return redirect('disciplinas')

        return render(request, 'disciplinas.html', {'form': form, 'disciplinas':disciplinas})