from django.urls import path
from .views import ajax_load_districts, ajax_load_upazila
urlpatterns = [
    path('distict', ajax_load_districts, name='ajax_load_districts'),
    path('upazila', ajax_load_upazila, name='ajax_load_upazilas'),
]