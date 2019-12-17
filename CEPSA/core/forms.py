from django.forms import ModelForm, Select, NumberInput, DateTimeInput, TextInput, SelectDateWidget, Textarea, FileInput, DateInput
from core.models import Curso, Disciplina, Aluno, Turma

class CursoForm(ModelForm):

    class Meta:
        model = Curso
        fields = ('nome', 'descricao',)
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control'}),
            'descricao': Textarea(attrs={'class': 'form-control'}),
        }

class DisciplinaForm(ModelForm):

    class Meta:
        model = Disciplina
        fields = ('nome', 'descricao',)
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control'}),
            'descricao': Textarea(attrs={'class': 'form-control'}),
        }

class RegistraAlunoForm(ModelForm):

    class Meta:
        model = Aluno
        fields = ('nome', 'data_nascimento','sexo','telefone',)
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control'}),
            'telefone': TextInput(attrs= {'class': 'form-control', 'placeholder': '(99) 99999999', 'data-mask':"(99) 99999999"}),
            'data_nascimento':DateInput(attrs= {'class': 'form-control', 'type': 'date'}),
            'sexo':Select(attrs={'class': 'form-control'}),
        }

class TurmaForm(ModelForm):

    class Meta:
        model = Turma
        fields = ('curso', 'ministrante','disciplina','carga_horaria',)
        widgets = {
            'curso': Select(attrs={'class': 'form-control'}),
            'ministrante': Select(attrs= {'class': 'form-control'}),
            'disciplina':Select(attrs= {'class': 'form-control'}),
            'carga_horaria':NumberInput(attrs={'class': 'form-control'}),
        }