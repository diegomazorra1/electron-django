"""SASRU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = staticfiles_urlpatterns()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('banco/', include ('apps.banco.urls', namespace="banco")),
    path('Rfid/', include ('apps.Rfid.urls', namespace="rfid")),
    path('usuarios/', include ('apps.usuarios.urls', namespace="usuarios")),
    path('', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/reset/password_reset', auth_views.PasswordResetView.as_view(), name= 'password_reset'),
    #auth_views.PasswordResetForm.as_view(),
    path('accounts/reset/password_reset_confirm', auth_views.PasswordChangeDoneView.as_view(), name= 'password_reset_done'),
     path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name= 'password_reset_confirm'),
    path('accounts/reset/done', auth_views. PasswordResetCompleteView.as_view(), name= 'password_reset_complete'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
