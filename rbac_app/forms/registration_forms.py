from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from . import choices
from organization_app.models import organization_models



class SuperUserCreateMotherAdminForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('mother_organization', 'username', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mother_organization'].empty_label = "--SELECT--"
        self.fields['mother_organization'].required = True
        
        if 'mother_organization' in self.data:
            try:
                mother_organization_id = int(self.data.get('mother_organization'))
                self.fields['mother_organization'].queryset = organization_models.MotherOrganizations.objects.filter(id=mother_organization_id).order_by('name_en')
            except (ValueError, TypeError):
                pass


class SuperUserCreateSisterAdminForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('mother_organization', 'sister_organization', 'username', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mother_organization'].empty_label = "--SELECT--"
        self.fields['sister_organization'].empty_label = "--SELECT--"

        self.fields['mother_organization'].required = True
        self.fields['sister_organization'].required = True

        self.fields['sister_organization'].queryset = organization_models.SisterOrganizations.objects.none()

        if 'mother_organization' in self.data and 'sister_organization' in self.data:
            try:
                mother_organization_id = int(self.data.get('mother_organization'))
                sister_organization_id = int(self.data.get('sister_organization'))
                self.fields['mother_organization'].queryset = organization_models.MotherOrganizations.objects.filter(id=mother_organization_id).order_by('name_en')
                self.fields['sister_organization'].queryset = organization_models.SisterOrganizations.objects.filter(id=sister_organization_id).order_by('name_english')
            except (ValueError, TypeError):
                pass


class SuperUserCreateBranchRegularAdminForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=choices.user_type_branch_or_regular,initial='--SELECT--')
    class Meta:
        model = get_user_model()
        fields = ('mother_organization', 'sister_organization', 'branch', 'user_type', 'username', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mother_organization'].empty_label = "--SELECT--"
        self.fields['sister_organization'].empty_label = "--SELECT--"
        self.fields['branch'].empty_label = "--SELECT--"

        self.fields['mother_organization'].required = True
        self.fields['sister_organization'].required = True
        self.fields['branch'].required = True

        self.fields['sister_organization'].queryset = organization_models.SisterOrganizations.objects.none()
        self.fields['branch'].queryset = organization_models.Branches.objects.none()

        if 'mother_organization' in self.data and 'sister_organization' in self.data and 'branch' in self.data:
            try:
                mother_organization_id = int(self.data.get('mother_organization'))
                sister_organization_id = int(self.data.get('sister_organization'))
                branch_id = int(self.data.get('branch'))
                self.fields['mother_organization'].queryset = organization_models.MotherOrganizations.objects.filter(id=mother_organization_id).order_by('name_en')
                self.fields['sister_organization'].queryset = organization_models.SisterOrganizations.objects.filter(id=sister_organization_id).order_by('name_english')
                self.fields['branch'].queryset = organization_models.Branches.objects.filter(id=branch_id).order_by('name_english')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset






