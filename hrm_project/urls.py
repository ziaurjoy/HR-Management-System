
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard_app.urls')),
    path('organization/', include('organization_app.urls')),
]
