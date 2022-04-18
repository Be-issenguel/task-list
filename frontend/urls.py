from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm

app_name = 'tasks'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('accounts/new/', views.CreateAccountView.as_view(), name='new-account'),
    path('accounts/create/', views.register_user, name='create-account'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html',
                                                         extra_context={'form': AuthenticationForm()}), name='login'),
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),
    path('<int:id>/accounts/edit/', views.EditProfileView.as_view(), name='edit-profile'),
    path('<int:id>/accounts/update', views.update_profile, name='update-profile'),
]
