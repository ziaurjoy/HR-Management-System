from django import forms
from address_app.models import Divisions, Districts, Upazilas
from ..models import organization_models
from .choiceses import choicess_has_concern

class SuperUserSisterOrganizationCreateForm(forms.ModelForm):
    has_branch_concern = forms.ChoiceField(choices=choicess_has_concern, widget=(forms.RadioSelect(attrs={'class': 'inline'})))
    class Meta:
        model = organization_models.SisterOrganizations
        fields = '__all__'
        labels = {
            'name_english' : "Name(English)",
            'name_banglali' : "Name(Bengali)",
        }
        widgets = {
                "has_branch_concern": forms.RadioSelect(attrs={"class": "inline"}),
            }
        error_messages = {
            'name_english': {
                'unique': ("Sister Organization Name Already Exists"),
            },
            'name_banglali': {
                'unique': ("Sister Organization Already Exists"),
            },
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['division'].empty_label = "--SELECT--"
        self.fields['district'].empty_label = "--SELECT--"
        self.fields['upazila'].empty_label = "--SELECT--"
        self.fields['mother_organization'].empty_label = "--SELECT--"
        
        self.fields['division'].queryset = Divisions.objects.all().order_by('name_english')
        self.fields['district'].queryset = Districts.objects.none()
        self.fields['upazila'].queryset = Upazilas.objects.none()
        
        if 'division' in self.data  and 'district' in self.data:
        
            division_id = int(self.data.get('division'))
            district_id = int(self.data.get('district'))
            self.fields['district'].queryset = Districts.objects.filter(division__id=division_id).order_by('name_english')
            self.fields['upazila'].queryset = Upazilas.objects.filter(district__id=district_id).order_by('name_english')
         


class SuperUserSisterOrganizationUpdateForm(forms.ModelForm):
    has_branch_concern = forms.ChoiceField(choices=choicess_has_concern, widget=(forms.RadioSelect(attrs={'class': 'inline'})))
    class Meta:
        model = organization_models.SisterOrganizations
        fields = '__all__'
        labels = {
            'name_english' : "Name(English)",
            'name_banglali' : "Name(Bengali)",
        }
        widgets = {
                "has_branch_concern": forms.RadioSelect(attrs={"class": "inline"}),
            }
        error_messages = {
            'name_english': {
                'unique': ("Sister Organization Name Already Exists"),
            },
            'name_banglali': {
                'unique': ("Sister Organization Already Exists"),
            },
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['division'].empty_label = "--SELECT--"
        self.fields['district'].empty_label = "--SELECT--"
        self.fields['upazila'].empty_label = "--SELECT--"
        self.fields['mother_organization'].empty_label = "--SELECT--"
        
        # self.fields['division'].queryset = Divisions.objects.all().order_by('name_english')
        # self.fields['district'].queryset = Districts.objects.none()
        # self.fields['upazila'].queryset = Upazilas.objects.none()
        
        if 'division' in self.data  and 'district' in self.data:
        
            division_id = int(self.data.get('division'))
            district_id = int(self.data.get('district'))
            self.fields['district'].queryset = Districts.objects.filter(division__id=division_id).order_by('name_english')
            self.fields['upazila'].queryset = Upazilas.objects.filter(district__id=district_id).order_by('name_english')
         