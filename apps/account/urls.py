from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

# app_name = 'account'

urlpatterns = [
    # account/login/  (personalizada)
    # path('login/', views.user_login, name='login'),

    # VISTAS DEL FRAMEWORK DE AUTENTICACION DE DJANGO:
    # Entrar
    # Salir
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # cambiar contraseñas para usuarios ya logiados:
    # 📧 Pide el email
    # ✅ Confirmación
    # path('password-change/', auth_views.PasswordChangeView.as_view(), name='password-change' ),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Restablecimiento de contraseña para usuarios NO logiados:
    # 📧 Pide el email
    # ✅ Confirmación
    # 🔐 Link del email
    # 🎉 Completado
    # path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    # Importar TODAS las rutas de autenticación de Django de una sola vez:
    # /login/
    # /logout/
    # /password_change/
    # /password_change/done/
    # /password_reset/
    # /password_reset/done/
    # /password_reset/<uidb64>/<token>/
    # /password_reset/complete/
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    

    # PAGINAS DEL SITIO:
    # account/
    path('', views.dashboard, name='dashboard')
]