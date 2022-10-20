from django.urls import path
from .views import dashboard_views

urlpatterns = [
    path('', dashboard_views.dashboard_views, name = 'dashboard'),
]