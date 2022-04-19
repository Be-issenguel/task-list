from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, TaskForm
from django.contrib.auth.models import User
from apps.tasks.models import Task, Attachment


# Tasks views.
class IndexView(View):
    def get(self, request):
        tasks = Task.objects.filter(user__id=request.user.id)
        ctx = {
            'tasks': tasks
        }
        return render(request, 'frontend/index.html', context=ctx)


# Accounts views
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
            return redirect('/')
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


class ProfileView(View):
    def get(self, request):
        return render(request, 'registration/profile.html')


class EditProfileView(View):
    def get(self, request, id):
        user = get_object_or_404(User, pk=id)
        ctx = {
            'form': UserForm(instance=user),
            'id': id,
        }
        return render(request, 'registration/edit.html', context=ctx)


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


class NewTaskView(View):
    def get(self, request):
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
            return redirect('/')
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


class EditTaskView(View):
    def get(self, request, id):
        task = get_object_or_404(Task, pk=id)
        ctx = {
            'form': TaskForm(instance=task),
            'id': task.id,
        }
        return render(request, 'frontend/edit-task.html', context=ctx)


def update_task(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
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


def delete_task(request, id):
    Task.objects.get(pk=id).delete()
    return redirect('/')


class IndexAttachmentView(View):
    def get(self, request, id):
        ctx = {
            'attachments': Attachment.objects.filter(task__id=id)
        }
        return render(request, 'frontend/attachments.html', context=ctx)
