from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from ..forms import mother_organization_forms
from ..models import organization_models



@login_required
def mother_organization_create_view(request):
    if request.user.is_superuser == True:
        form = mother_organization_forms.MotherOrganizationCreateForms()
        if request.method == "POST":
            form = mother_organization_forms.MotherOrganizationCreateForms(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Mother Organization Created !!')
                return redirect('mother-organization-index')
            else:
                messages.error(request, form.errors)
        context = {
            'form': form
            }
        return render(request, 'organization_app/mother_organization/create.html',context)
    else:
        return render(request, 'rbac_app/permission/forbidden_template/forbidden.html')


@login_required
def mother_organization_index_view(request):
    if request.user.is_superuser == True:
        mother_organization_list = organization_models.MotherOrganizations.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(mother_organization_list, 2)
        try:
            mother_organizations = paginator.page(page)
        except PageNotAnInteger:
            mother_organizations = paginator.page(1)
        except EmptyPage:
            mother_organizations = paginator.page(paginator.num_pages)
        context = {
            'mother_organizations_list': mother_organizations,
            }
        return render(request, 'organization_app/mother_organization/index.html',context)
    else:
        return render(request, 'rbac_app/permission/forbidden_template/forbidden.html')


@login_required
def mother_organization_update_view(request, pk):
    if request.user.is_superuser == True:
        # get_mother_organization = mother_organization_models.MotherOrganizations.objects.get(id=pk)
        get_mother_organization = get_object_or_404(organization_models.MotherOrganizations, id=pk)
        form = mother_organization_forms.MotherOrganizationUpdateForms(instance=get_mother_organization)
        if request.method == "POST":
            form = mother_organization_forms.MotherOrganizationUpdateForms(request.POST, instance=get_mother_organization)
            if form.is_valid():
                form.save()
                messages.success(request, 'Mother Organization Updated !!')
                return redirect('mother-organization-index')
            else:
                messages.error(request, form.errors)
        context = {
            'form': form
            }
        return render(request, 'organization_app/mother_organization/update.html',context)
    else:
        return render(request, 'rbac_app/permission/forbidden_template/forbidden.html')


@login_required
def mother_organization_delete_view(request,pk):
    if request.user.is_superuser == True:
        try:
            get_mother_organization = get_object_or_404(organization_models.MotherOrganizations, id=pk)
            get_mother_organization.delete()
            messages.success(request, 'Mother Organization !!')
            return redirect('mother-organization-index')
        except:
            messages.error(request, 'Mother Organization not possible !!')
            return redirect('mother-organization-index')
    else:
        return render(request, 'rbac_app/permission/forbidden_template/forbidden.html')
