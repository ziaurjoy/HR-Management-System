from django import forms
from address_app.models import Divisions, Districts, Upazilas
from ..models import organization_models

class SuperUserBranchCreateForm(forms.ModelForm):
    class Meta:
        model = organization_models.Branches
        fields = '__all__'
        labels = {
            'name_english' : "Name(English)",
            'name_banglali' : "Name(Bengali)",
        }
        error_messages = {
            'name_english': {
                'unique': ("Branch Name Already Exists"),
            },
            'name_banglali': {
                'unique': ("Branch Already Exists"),
            },
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mother_organization'].empty_label = "--SELECT--"
        self.fields['sister_organization'].empty_label = "--SELECT--"
        self.fields['division'].empty_label = "--SELECT--"
        self.fields['district'].empty_label = "--SELECT--"
        self.fields['upazila'].empty_label = "--SELECT--"

        self.fields['mother_organization'].queryset = organization_models.MotherOrganizations.objects.all().order_by('name_en')
        self.fields['sister_organization'].queryset = organization_models.SisterOrganizations.objects.none()
        self.fields['division'].queryset = Divisions.objects.all().order_by('name_english')
        self.fields['district'].queryset = Districts.objects.none()
        self.fields['upazila'].queryset = Upazilas.objects.none()
        
        if 'mother_organization' in self.data and 'sister_organization' in self.data and 'division' in self.data  and 'district' in self.data and 'upazila' in self.data:
            mother_organization_id = int(self.data.get('mother_organization'))
            sister_organization_id = int(self.data.get('sister_organization'))
            division_id = int(self.data.get('division'))
            district_id = int(self.data.get('district'))
            upazila_id = int(self.data.get('upazila'))

            self.fields['mother_organization'].queryset = organization_models.MotherOrganizations.objects.filter(id=mother_organization_id)
            self.fields['sister_organization'].queryset = organization_models.SisterOrganizations.objects.filter(id=sister_organization_id)
            self.fields['division'].queryset = Divisions.objects.filter(id=division_id)
            self.fields['district'].queryset = Districts.objects.filter(id=district_id)
            self.fields['upazila'].queryset = Upazilas.objects.filter(id=upazila_id)
         


class SuperUserBranchUpdateForm(forms.ModelForm):
    class Meta:
        model = organization_models.Branches
        fields = '__all__'
        labels = {
            'name_english' : "Name(English)",
            'name_banglali' : "Name(Bengali)",
        }
        error_messages = {
            'name_english': {
                'unique': ("Branch Name Already Exists"),
            },
            'name_banglali': {
                'unique': ("Branch Already Exists"),
            },
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mother_organization'].empty_label = "--SELECT--"
        self.fields['sister_organization'].empty_label = "--SELECT--"
        self.fields['division'].empty_label = "--SELECT--"
        self.fields['district'].empty_label = "--SELECT--"
        self.fields['upazila'].empty_label = "--SELECT--"

        self.fields['mother_organization'].queryset = organization_models.MotherOrganizations.objects.all().order_by('name_en')
        self.fields['division'].queryset = Divisions.objects.all().order_by('name_english')

        if 'mother_organization' in self.data and 'sister_organization' in self.data and 'division' in self.data  and 'district' in self.data and 'upazila' in self.data:
            mother_organization_id = int(self.data.get('mother_organization'))
            sister_organization_id = int(self.data.get('sister_organization'))
            division_id = int(self.data.get('division'))
            district_id = int(self.data.get('district'))
            upazila_id = int(self.data.get('upazila'))

            self.fields['mother_organization'].queryset = organization_models.MotherOrganizations.objects.filter(id=mother_organization_id)
            self.fields['sister_organization'].queryset = organization_models.SisterOrganizations.objects.filter(id=sister_organization_id)
            self.fields['division'].queryset = Divisions.objects.filter(id=division_id)
            self.fields['district'].queryset = Districts.objects.filter(id=district_id)
            self.fields['upazila'].queryset = Upazilas.objects.filter(id=upazila_id)
         