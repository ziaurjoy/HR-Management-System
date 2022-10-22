from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from ..forms import sister_organization_forms
from ..models import organization_models
from address_app.models import Districts, Upazila



# @login_required
def sister_organization_create_view(request):
    form = sister_organization_forms.SuperUserSisterOrganizationCreateForm()
    if request.method == "POST":
        form = sister_organization_forms.SuperUserSisterOrganizationCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sister Organization Created !!')
            return redirect('sister-organization-index')
        else:
            messages.error(request, form.errors)
    context = {
        'form': form
        }
    return render(request, 'organization_app/sister_organization/superuser/create.html',context)



def sister_organization_index_view(request):
    sister_organization_list = organization_models.SisterOrganizations.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(sister_organization_list, 20)
    try:
        sister_organizations = paginator.page(page)
    except PageNotAnInteger:
        sister_organizations = paginator.page(1)
    except EmptyPage:
        sister_organizations = paginator.page(paginator.num_pages)
    context = {
        'sister_organization_list': sister_organizations,
        }
    return render(request, 'organization_app/sister_organization/superuser/index.html',context)



def sister_organization_update_view(request, pk):
    get_sister_organization = organization_models.SisterOrganizations.objects.get(id=pk)
    get_sister_organization = get_object_or_404(organization_models.SisterOrganizations, id=pk)
    form = sister_organization_forms.SuperUserSisterOrganizationUpdateForm(instance=get_sister_organization)
    form.fields['district'].queryset = Districts.objects.filter(division__id=get_sister_organization.division.id)
    form.fields['upazila'].queryset = Upazila.objects.filter(district__id=get_sister_organization.district.id)
    if request.method == "POST":
        form = sister_organization_forms.SuperUserSisterOrganizationUpdateForm(request.POST, instance=get_sister_organization)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sister Organization Updated !!')
            return redirect('sister-organization-index')
        else:
            messages.error(request, form.errors)
    context = {
        'form': form
        }
    return render(request, 'organization_app/sister_organization/superuser/update.html',context)



def sister_organization_delete_view(request,pk):
    try:
        get_sister_organization = get_object_or_404(organization_models.SisterOrganizations, id=pk)
        get_sister_organization.delete()
        messages.success(request, 'Sister Organization !!')
        return redirect('sister-organization-index')
    except:
        messages.error(request, 'Sister Organization not possible !!')
        return redirect('sister-organization-index')
