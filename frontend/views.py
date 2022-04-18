from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm


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
        return render(request, 'frontend/accounts-new.html', context=ctx)


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
            return render(request, 'frontend/accounts-new.html', context=ctx)
    else:
        ctx = {
            'form': UserCreationForm(),
        }
        return render(request, 'frontend/accounts-new.html', context=ctx)
