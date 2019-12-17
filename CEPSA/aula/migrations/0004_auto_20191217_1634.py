# Generated by Django 2.0 on 2019-12-17 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0003_aula_turma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aula',
            name='ocorecia',
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='aula',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ocorrencias', to='aula.Aula'),
        ),
    ]
