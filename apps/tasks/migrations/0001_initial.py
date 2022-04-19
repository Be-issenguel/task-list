# Generated by Django 4.0.3 on 2022-04-19 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='task name')),
                ('description', models.TextField(verbose_name='task description')),
                ('limit_date', models.DateField(verbose_name='task limit date')),
                ('priority', models.CharField(choices=[('Baixa', 1), ('Média', 2), ('Alta', 3)], max_length=5, verbose_name='task priority')),
                ('is_finished', models.BooleanField(default=False, verbose_name='task is finished')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='attachment name')),
                ('file', models.FileField(upload_to='C:\\laragon\\www\\python\\task-list\\.media', verbose_name='attachment file')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]
