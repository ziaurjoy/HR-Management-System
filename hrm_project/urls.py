
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard_app.urls')),
    path('organization/', include('organization_app.urls')),
    path('address/', include('address_app.urls')),
    path('rbac/', include('rbac_app.urls')),


    path('login/', auth_views.LoginView.as_view(template_name='login_page/login.html'), name = 'login' ),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    
    # path('password-reset/', reset_password, name = 'reset_password'),
    # path("password_reset", reset_password_views.password_reset_request, name="password_reset"),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration_app/resert_password/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration_app/resert_password/password_reset_confirm.html"), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration_app/resert_password/password_reset_complete.html'), name='password_reset_complete'),
]
