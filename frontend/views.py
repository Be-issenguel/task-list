from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from django.contrib.auth.models import User


# Tasks views.
class IndexView(View):
    def get(self, request):
        return render(request, 'frontend/index.html')


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


