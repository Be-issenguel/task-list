from django.forms import ModelForm
from django.contrib.auth.models import User
from apps.tasks.models import Task, Attachment


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 5})
        self.fields['limit_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['priority'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Task
        exclude = ['user']


class AttachmentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['file'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Attachment
        exclude = ['task']
