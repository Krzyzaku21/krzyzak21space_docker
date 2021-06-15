from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('password_change/', PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path(
        'password_change/done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path(
        'reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    path(
        'reset/done/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit, name='edit'),
    path('register/', views.register, name="register"),
    # path('register_done/', TemplateView.as_view(template_name="register_done.html"), name="register_done"),
    path('gallery/', TemplateView.as_view(template_name="gallery.html"), name="gallery"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="logout"),
]
