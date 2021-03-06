from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, TaskForm, AttachmentForm
from django.contrib.auth.models import User
from apps.tasks.models import Task, Attachment


class WelcomeView(View):
    def get(self, request):
        return render(request, 'frontend/welcome.html')


@login_required()
def index(request):
    tasks = Task.objects.filter(user__id=request.user.id)
    ctx = {
        'tasks': tasks
    }
    return render(request, 'frontend/index.html', context=ctx)


class CreateAccountView(View):
    def get(self, request):
        ctx = {
            'form': UserCreationForm(),
        }
        return render(request, 'registration/new.html', context=ctx)


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
        else:
            ctx = {
                'form': UserCreationForm(),
                'errors': form.errors,
            }
            return render(request, 'registration/new.html', context=ctx)
    else:
        ctx = {
            'form': UserCreationForm(),
        }
        return render(request, 'registration/new.html', context=ctx)


@login_required()
def profile(request):
    return render(request, 'registration/profile.html')


@login_required()
def edit_profile(request, id):
    user = get_object_or_404(User, pk=id)
    ctx = {
        'form': UserForm(instance=user),
        'id': id,
    }
    return render(request, 'registration/edit.html', context=ctx)


@login_required()
def update_profile(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
        else:
            ctx = {
                'form': form,
                'id': id,
            }
            return render(request, 'registration/edit.html', context=ctx)
    else:
        ctx = {
            'form': UserForm(instance=user),
            'id': id,
        }
        return render(request, 'registration/edit.html', context=ctx)


@login_required()
def new_task(request):
    ctx = {
        'form': TaskForm()
    }
    return render(request, 'frontend/new-task.html', context=ctx)


@login_required
def store_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            task = form.save(commit=False)
            task.user_id = request.user.id
            task.save()
            return redirect('/tasks/index/')
        else:
            ctx = {
                'form': form,
                'errors': form.errors,
            }
            return render(request, 'frontend/new-task.html', context=ctx)
    else:
        ctx = {
            'form': TaskForm()
        }
        return render(request, 'frontend/new-task.html', context=ctx)


@login_required()
def edit_task(request, id):
    task = get_object_or_404(Task, pk=id)
    ctx = {
        'form': TaskForm(instance=task),
        'id': task.id,
    }
    return render(request, 'frontend/edit-task.html', context=ctx)


@login_required()
def update_task(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/tasks/index/')
        else:
            ctx = {
                'form': form,
                'errors': form.errors,
            }
            return render(request, 'frontend/edit-task.html', context=ctx)
    else:
        ctx = {
            'form': TaskForm(instance=task),
            'id': task.id,
        }
        return render(request, 'frontend/edit-task.html', context=ctx)


@login_required()
def delete_task(request, id):
    Task.objects.get(pk=id).delete()
    return redirect('/tasks/index/')


@login_required()
def attachments(request, id):
    ctx = {
        'attachments': Attachment.objects.filter(task__id=id),
        'task': get_object_or_404(Task, pk=id)
    }
    return render(request, 'frontend/attachments.html', context=ctx)


@login_required()
def new_attachment(request, id):
    ctx = {
        'form': AttachmentForm,
        'task': get_object_or_404(Task, pk=id),
    }
    return render(request, 'frontend/new-attachment.html', context=ctx)


@login_required()
def store_attachment(request, id):
    if request.method == 'POST':
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            attachment = form.save(commit=False)
            attachment.task_id = id
            attachment.save()
            return redirect(f'/{id}/tasks/attachments/')
        else:
            ctx = {
                'form': AttachmentForm,
                'id': id,
            }
            return render(request, 'frontend/new-attachment.html', context=ctx)
    else:
        ctx = {
            'attachments': Attachment.objects.filter(task__id=id),
            'id': id
        }
        return render(request, 'frontend/attachments.html', context=ctx)


@login_required()
def delete_attachment(request, id):
    attachment = Attachment.objects.filter(pk=id).get()
    task_id = attachment.task_id
    attachment.delete()
    return redirect(f'/{task_id}/tasks/attachments')
