
from rbac_app.forms import permission_forms
from django.shortcuts import render, redirect
from rbac_app.models import permission_models, users_models
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# @login_required
# def user_wise_permissions_view(request):
#     form = permission_forms.SuperUserUserWisePermissionsForm()
#     if request.method == "POST": 
#         form = permission_forms.SuperUserUserWisePermissionsForm(request.POST)
#         print(form.errors)
#         if form.is_valid():
#             user = form.cleaned_data['user']
#             mother_organization_id = form.cleaned_data['mother_organization']
#             sister_organization_id = form.cleaned_data['sister_organization']
#             branch_id = form.cleaned_data['branch']
#             permission_list = request.POST.getlist('permission')
#             query_permission = permission_models.UserPermissions.objects.filter(user__id = user.id)
#             for permission in query_permission:
#                 if permission.permission in permission_list:
#                     continue
#                 else:
#                     permission.delete()
            
#             for permission in permission_list:
#                 permission_models.UserPermissions.objects.create(
#                     user=user, 
#                     permission=permission, 
#                     mother_organization=mother_organization_id,
#                     sister_organization=sister_organization_id,
#                     branch = branch_id
#                     )
#             # messages.success(request, 'Permissions Set !!')
#             # return redirect('user-wise-permission')
#         context = {
#             'form': form,
#         }
#         return render(request, 'rbac_app/permission/permissions.html',context)

#     context = {
#         'form': form,
#     }
#     return render(request, 'rbac_app/permission/permissions.html',context)




@login_required
def user_wise_permissions_view(request):
    form = permission_forms.SuperUserUserWisePermissionsForm()
    permission_list = []
    if request.method == "POST": 
        form = permission_forms.SuperUserUserWisePermissionsForm(request.POST)   
        if form.is_valid():
            print('Print valid forms')
            user = form.cleaned_data['user']
            mother_organization_id = form.cleaned_data['mother_organization']
            sister_organization_id = form.cleaned_data['sister_organization']
            branch_id = form.cleaned_data['branch']
            permission_list = request.POST.getlist('permission')

            query_permission = permission_models.UserPermissions.objects.filter(user__id = user.id)
            for permissions in query_permission:
                if permissions.permission in permission_list:
                    # continue
                    permissions.delete()
                else:
                    permissions.delete()
            
            for permission in permission_list:
                try:
                    permission_models.UserPermissions.objects.create(
                        user=user, 
                        permission=permission, 
                        mother_organization=mother_organization_id,
                        sister_organization=sister_organization_id,
                        branch = branch_id
                        )
                except:
                    continue
            context = {
                'form': form,
            }
            return render(request, 'rbac_app/permission/permissions.html',context) 
        
    context = {
        'form': form,
    }
    return render(request, 'rbac_app/permission/permissions.html',context)




def load_user_wise_permission(request):
    user = request.GET.get('userId')
    user = int(user)
    current_permission = []
    permissions = permission_models.UserPermissions.objects.filter(user__id=user)
    for permission in permissions:
        current_permission.append(permission.permission)
    context = {
        'current_permission': current_permission,
        'permission_list': permissions
    }
    return render(request, 'rbac_app/permission/permission_template.html', context)




