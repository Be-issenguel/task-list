from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('accounts/new/', views.CreateAccountView.as_view(), name='new-account'),
    path('accounts/create/', views.register_user, name='create-account'),
]
