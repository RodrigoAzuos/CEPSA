from django.forms import ModelForm, Select, NumberInput, DateTimeInput, TextInput, SelectDateWidget, Textarea, FileInput
from aula.models import Aula

class AulaForm(ModelForm):

    class Meta:
        model = Aula
        fields = ('material', 'aulas_ministradas', 'data', 'assunto', 'descricao',)
        widgets = {
            'aulas_ministradas': NumberInput(attrs={'class': 'form-control'}),
            'data': DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'assunto': TextInput(attrs={'class': 'form-control'}),
            'descricao': Textarea(attrs={'class': 'form-control'}),
            'material': FileInput(attrs={'class': 'form-control'}),
        }
