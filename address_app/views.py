from django.shortcuts import render
from .models import Districts, Upazilas
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def ajax_load_districts(request):
    division_id = request.GET.get('division')
    districts = Districts.objects.filter(division__id=division_id).order_by('name_english')
    return render(request, 'address_app/load_district_options.html', {'districts': districts})


@login_required
def ajax_load_upazila(request):
    district_id = request.GET.get('district')
    upazilas = Upazilas.objects.filter(district__id=district_id).order_by('name_english')
    return render(request, 'address_app/load_upazila_options.html', {'upazilas': upazilas})