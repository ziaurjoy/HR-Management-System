

from django.shortcuts import  render, redirect
from ..forms import registration_forms
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from ..models import users_models


@login_required
def registration_mother_admin_create_view(request):
    if request.user.is_superuser == True:
        form = registration_forms.SuperUserCreateMotherAdminForm()
        if request.method == "POST":
            form = registration_forms.SuperUserCreateMotherAdminForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_type = 'Mother Organization Admin'
                form.save()
                messages.success(request, 'Registration Successfully Created !!')
                return redirect('branch-index')
            else:
                messages.error(request, form.errors)
        context = {
            'form': form
            }
        return render(request, 'rbac_app/registration/superuser/mother_admin/create.html',context)
    else:
        return render(request, 'rbac_app/permission/forbidden_template/forbidden.html')



@login_required
def registration_sister_admin_create_view(request):
    if request.user.user_type == 'Mother Organization Admin' or request.user.is_superuser == True:
        form = registration_forms.SuperUserCreateSisterAdminForm()
        if request.method == "POST":
            form = registration_forms.SuperUserCreateSisterAdminForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_type = 'Sister Organization Admin'
                form.save()
                messages.success(request, 'Registration Successfully Created !!')
                return redirect('branch-index')
            else:
                messages.error(request, form.errors)
        context = {
            'form': form
            }
        return render(request, 'rbac_app/registration/superuser/sister_admin/create.html',context)
    else:
        return render(request, 'rbac_app/permission/forbidden_template/forbidden.html')



@login_required
def registration_branch_admin_create_view(request):
    if request.user.user_type == 'Sister Organization Admin' or request.user.user_type == 'Mother Organization Admin' or request.user.is_superuser == True:
        form = registration_forms.SuperUserCreateBranchRegularAdminForm()
        if request.method == "POST":
            form = registration_forms.SuperUserCreateBranchRegularAdminForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Registration Successfully Created !!')
                return redirect('branch-index')
            else:
                messages.error(request, form.errors)
        context = {
            'form': form
            }
        return render(request, 'rbac_app/registration/superuser/branch_admin/create.html',context)
    else:
        return render(request, 'rbac_app/permission/forbidden_template/forbidden.html')



def load_branch_user(request):
    branch_id = request.GET.get('branchId')
    user_list = users_models.Users.objects.filter(branch__id=branch_id)
    return render(request, 'rbac_app/registration/load_user/load_user.html', {'user_list': user_list})








