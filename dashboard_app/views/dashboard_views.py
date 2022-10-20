from django.shortcuts import render

def dashboard_views(request):
  return render(request, 'dashboard/dashboard.html')


