from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from ..forms import branch_forms
from ..models import organization_models
from address_app.models import Districts, Upazilas



@login_required
def branch_create_view(request):
    if request.user.user_type == 'Sister Organization Admin' or request.user.user_type == 'Mother Organization Admin' or request.user.is_superuser == True:
        form = branch_forms.SuperUserBranchCreateForm()
        if request.method == "POST":
            form = branch_forms.SuperUserBranchCreateForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Branch Created !!')
                return redirect('branch-index')
            else:
                messages.error(request, form.errors)
        context = {
            'form': form
            }
        return render(request, 'organization_app/branch/superuser/create.html',context)
    else:
        return render(request, 'rbac_app/permission/forbidden_template/forbidden.html')


@login_required
def branch_index_view(request):
    if request.user.user_type == 'Sister Organization Admin' or request.user.user_type == 'Mother Organization Admin' or request.user.is_superuser == True:
        branch_list = organization_models.Branches.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(branch_list, 20)
        try:
            branchs = paginator.page(page)
        except PageNotAnInteger:
            branchs = paginator.page(1)
        except EmptyPage:
            branchs = paginator.page(paginator.num_pages)
        context = {
            'branch_list': branchs,
            }
        return render(request, 'organization_app/branch/superuser/index.html',context)
    else:
        return render(request, 'rbac_app/permission/forbidden_template/forbidden.html')


@login_required
def branch_update_view(request, pk):
    if request.user.user_type == 'Sister Organization Admin' or request.user.user_type == 'Mother Organization Admin' or request.user.is_superuser == True:
        get_branch = organization_models.Branches.objects.get(id=pk)
        get_branch = get_object_or_404(organization_models.Branches, id=pk)
        form = branch_forms.SuperUserBranchUpdateForm(instance=get_branch)
        form.fields['district'].queryset = Districts.objects.filter(division__id=get_branch.division.id)
        form.fields['upazila'].queryset = Upazilas.objects.filter(district__id=get_branch.district.id)
        if request.method == "POST":
            form = branch_forms.SuperUserBranchUpdateForm(request.POST, instance=get_branch)
            if form.is_valid():
                form.save()
                messages.success(request, 'Branch Updated !!')
                return redirect('branch-index')
            else:
                messages.error(request, form.errors)
        context = {
            'form': form
            }
        return render(request, 'organization_app/branch/superuser/update.html',context)
    else:
        return render(request, 'rbac_app/permission/forbidden_template/forbidden.html')


@login_required
def branch_delete_view(request,pk):
    if request.user.user_type == 'Sister Organization Admin' or request.user.user_type == 'Mother Organization Admin' or request.user.is_superuser == True:
        try:
            get_branch = get_object_or_404(organization_models.Branches, id=pk)
            get_branch.delete()
            messages.success(request, 'Branch !!')
            return redirect('branch-index')
        except:
            messages.error(request, 'Branch not possible !!')
            return redirect('branch-index')
    else:
        return render(request, 'rbac_app/permission/forbidden_template/forbidden.html')



@login_required
def ajax_load_branch(request):
    sister_organization_id = request.GET.get('sister_organization_id')
    branch_list = organization_models.Branches.objects.filter(sister_organization__id=sister_organization_id).order_by('name_english')
    return render(request, 'organization_app/branch/load_ajax_branches.html', {'branch_list': branch_list})



