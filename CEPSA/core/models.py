from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Base(models.Model):

	criado_em = models.DateTimeField('Criado em', auto_now_add=True, blank=False, null=False)
	atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		abstract = True

	def get_criado_em(self, format):
		return self.criado_em.__format__(format).__str__()

	def get_atualizado_em(self, format):
		return self.atualizado_em.__format__(format).__str__()

class Aluno(Base):

	SEXO_CHOICE = (
		('F', 'Feminino'),
		('M', 'Masculino'),
	)

	nome = models.CharField('Nome', max_length=128, null=False, blank=False)
	data_nascimento = models.DateField(null=False, blank=False)
	sexo = models.CharField('Nivel_conciencia', choices=SEXO_CHOICE, max_length=2, null=True,blank=True, default='A')
	telefone = models.CharField('Telefone', max_length=14, null=True, blank=True)

	class Meta:
		verbose_name = 'Aluno'
		verbose_name_plural = 'Alunos'

	def __str__(self):
		return self.nome

class Curso(Base):
	nome = models.CharField('Nome', max_length=128, null=False, blank=False)
	descricao = models.CharField('Descricao', max_length=512, null=False, blank=False)

	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'

	def __str__(self):
		return self.nome


class Matricula(Base):
	aluno = models.ForeignKey(Aluno, on_delete= models.CASCADE, related_name='matricula', null=False, blank=False)
	curso = models.ForeignKey(Curso, on_delete= models.CASCADE, null=False, blank=False)
	numero_matricula = models.IntegerField('Numero_matricula', null=False, blank=False)

	class Meta:
		verbose_name = 'Matricula'
		verbose_name_plural = 'Matriculas'

	def __str__(self):
		return self.numero_matricula

class Disciplina(Base):
	nome = models.CharField('Nome', max_length=128, null=False, blank=False)
	descricao = models.CharField('Descricao', max_length=512, null=False, blank=False)

	class Meta:
		verbose_name = 'Disciplina'
		verbose_name_plural = 'Disciplinas'

	def __str__(self):
		return self.nome

class Turma(Base):
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=False, related_name='Turmas')
	ministrante = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='Turmas')
	disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=False, blank=False, related_name='Turmas')
	carga_horaria = models.IntegerField('Carga_horaria', null=False, blank=False)
	alunos = models.ManyToManyField(Aluno, related_name='minhas_turmas')

	class Meta:
		verbose_name = 'Turma'
		verbose_name_plural = 'Turmas'

	def __str__(self):
		return "%s - %s " %(self.disciplina,self.ministrante)


