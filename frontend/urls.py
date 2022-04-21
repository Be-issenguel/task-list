from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

app_name = 'tasks'
urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome'),
    path('accounts/new/', views.CreateAccountView.as_view(), name='new-account'),
    path('accounts/create/', views.register_user, name='create-account'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html',
                                                         extra_context={'form': AuthenticationForm()}), name='login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('<int:id>/accounts/edit/', views.edit_profile, name='edit-profile'),
    path('<int:id>/accounts/update', views.update_profile, name='update-profile'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('accounts/change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change'
                                                                                          '-password.html'),
         name='password-change'),
    path('accounts/password-change-done',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('tasks/index/', views.index, name='index'),
    path('tasks/new/', views.new_task, name='new-task'),
    path('tasks/store/', views.store_task, name='store-task'),
    path('<int:id>/task/edit/', views.edit_task, name='edit-task'),
    path('<int:id>/tasks/update/', views.update_task, name='update-task'),
    path('<int:id>/tasks/delete/', views.delete_task, name='delete-task'),
    path('<int:id>/tasks/attachments/', views.attachments, name='attachments'),
    path('<int:id>/tasks/attachments/new/', views.new_attachment, name='new-attachment'),
    path('<int:id>/tasks/attachments/store/', views.store_attachment, name='store-attachment'),
    path('<int:id>/tasks/attachments/delete/', views.delete_attachment, name='delete-attachment'),
]
