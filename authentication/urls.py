from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path

from . import views

urlpatterns = [
    path(
        '',
        LoginView.as_view(template_name='authentication/login.html', redirect_authenticated_user=True),
        name='login',
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup_page, name='signup'),
    path(
        'change-password/',
        PasswordChangeView.as_view(template_name='authentication/change_password.html'),
        name='password_change',
    ),
    path(
        'change-password-done/',
        PasswordChangeDoneView.as_view(template_name='authentication/change_password_done.html'),
        name='password_change_done',
    ),
    path('upload_profile_picture/', views.upload_profile_picture, name='upload_profile_picture'),
]
