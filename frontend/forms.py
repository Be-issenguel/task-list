from django.forms import ModelForm
from django.contrib.auth.models import User
from apps.tasks.models import Task


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'limit_date', 'priority', 'is_finished']
