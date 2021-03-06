from django.db import models
from django.contrib.auth.models import User
from config.settings import MEDIA_ROOT, PRIORITY_CHOICES


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='task name')
    description = models.TextField(verbose_name='task description')
    limit_date = models.DateField(verbose_name='task limit date')
    priority = models.CharField(max_length=5, choices=PRIORITY_CHOICES, verbose_name='task priority')
    is_finished = models.BooleanField(default=False, verbose_name='task is finished')


class Attachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='attachment name')
    file = models.FileField(upload_to='', verbose_name='attachment file')
