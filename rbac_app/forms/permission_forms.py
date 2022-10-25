from django.contrib.auth import get_user_model
from django import forms
from rbac_app.models import permission_models, users_models
from organization_app.models import organization_models

class SuperUserUserWisePermissionsForm(forms.ModelForm):
    class Meta:
        model = permission_models.UserPermissions
        fields = '__all__'

        labels = {
            'user' : "User name",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['sister_organization'].required = True
        self.fields['branch'].required = True
        self.fields['user'].required = True

        self.fields['mother_organization'].empty_label = "--SELECT--"
        self.fields['sister_organization'].empty_label = "--SELECT--"
        self.fields['branch'].empty_label = "--SELECT--"
        self.fields['user'].empty_label = "--SELECT--"
        
        self.fields['mother_organization'].queryset = organization_models.MotherOrganizations.objects.all()
        self.fields['sister_organization'].queryset = organization_models.SisterOrganizations.objects.none()
        self.fields['branch'].queryset = organization_models.Branches.objects.none()
        self.fields['user'].queryset =users_models.Users.objects.none()
  
        if 'mother_organization' in self.data and 'sister_organization' in self.data and 'branch' in self.data:
            try:
                mother_organization_id = int(self.data.get('mother_organization'))
                sister_organization_id = int(self.data.get('sister_organization'))
                branch_id = int(self.data.get('branch'))
                self.fields['mother_organization'].queryset = organization_models.MotherOrganizations.objects.filter(id=mother_organization_id).order_by('name_en')
                self.fields['sister_organization'].queryset = organization_models.SisterOrganizations.objects.filter(id=sister_organization_id).order_by('name_english')
                self.fields['branch'].queryset = organization_models.Branches.objects.filter(id=branch_id).order_by('name_english')
                self.fields['user'].queryset = users_models.Users.objects.filter(branch__id=branch_id)
               

            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Permission queryset
        