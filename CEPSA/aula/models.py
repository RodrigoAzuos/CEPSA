from django.db import models

from core.models import Aluno
from core.models import Base, Turma
# Create your models here.

class Ocorrencia(Base):
	titulo = models.CharField('tirulo', max_length=128, null=False, blank=False)
	descricao = models.CharField('Descricao', max_length=128, null=False, blank=False)
	aula = models.ForeignKey('Aula', on_delete=models.CASCADE, null=True, blank=True, related_name='ocorrencias')

	class Meta:
		verbose_name = 'Ocorrencia'
		verbose_name_plural = 'Ocorrencias'

class Aula(Base):

	STATUS_CHOICE= (
		('pendente', 'pendente'),
		('em_andamento', 'Em andamento'),
		('finalizada', 'Finalizada'),
	)

	status  = models.CharField('Satus', choices=STATUS_CHOICE, max_length=14, default='pendente', null=False, blank=False)
	material =  models.FileField('Material', upload_to='material/%Y/', default='material/2019/', null=True, blank=True)
	aulas_ministradas = models.IntegerField('Aulas ministradas', null=False, blank=False)
	data = models.DateField(null=False, blank=False)
	assunto = models.CharField('Assunto', max_length=128, null=False, blank=False)
	descricao = models.CharField('Descricao', max_length=128, null=False, blank=False)
	frequencia = models.ManyToManyField(Aluno, related_name='aulas_assistidas')
	turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='aulas')

	class Meta:
		verbose_name = 'Aula'
		verbose_name_plural = 'Aulas'

