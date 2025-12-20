#from django.contrib import admin
from django.urls import path, include
#from django.shortcuts import render
from appls.usuario.views import CustomLoginView, dashboard , registro_usuario, CustomLogoutView

from django.contrib.auth import views as auth_views
from .forms import EmailLoginForm

urlpatterns = [
  
    path("login/", CustomLoginView.as_view(), name="login"),
        
        
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    
    path("registro/", registro_usuario, name="registro"),  
    
    
    # 🔹 Recuperación de contraseña
    path("password_reset/", 
         auth_views.PasswordResetView.as_view(
             template_name="usuario/password_reset.html",
             email_template_name="usuario/password_reset_email.html",
             subject_template_name="usuario/password_reset_subject.txt",
             success_url="/usuario/password_reset_done/"
         ), 
         name="password_reset"),

    path("password_reset_done/",
         auth_views.PasswordResetDoneView.as_view(
             template_name="usuario/password_reset_done.html"
         ),
         name="password_reset_done"),

    path("reset/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(
             template_name="usuario/password_reset_confirm.html",
             success_url="/usuario/reset_done/"
         ),
         name="password_reset_confirm"),

    path("reset_done/",
         auth_views.PasswordResetCompleteView.as_view(
             template_name="usuario/password_reset_complete.html"
         ),
         name="password_reset_complete"),

  
   path("dashboard/", dashboard, name="dashboard"),
   
    
    
]

