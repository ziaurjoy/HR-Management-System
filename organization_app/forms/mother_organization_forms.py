from django import forms
from ..models import organization_models
from .choiceses import choicess_has_concern

class MotherOrganizationCreateForms(forms.ModelForm):
    has_sister_concern = forms.ChoiceField(choices=choicess_has_concern, widget=(forms.RadioSelect(attrs={'class': 'inline'})))
    class Meta:
        model = organization_models.MotherOrganizations
        fields = ('__all__')
        labels = {
            'name_en' : "Name (English)",
            'name_bn' : "Name (Bengali)",
         }
        widgets = {
            "has_sister_concern": forms.RadioSelect(attrs={"class": "inline"}),
        }
        error_messages = {
            'name_en': {
                'unique': ("Mother Organization Name Already Exists"),
            },
            'name_bn': {
                'unique': ("Mother Organization Already Exists"),
            },

        }



class MotherOrganizationUpdateForms(forms.ModelForm):
    has_sister_concern = forms.ChoiceField(choices=choicess_has_concern, widget=(forms.RadioSelect(attrs={'class': 'inline'})))
    class Meta:
        model = organization_models.MotherOrganizations
        fields = '__all__'
        labels = {
            'name_en' : "Name (English)",
            'name_bn' : "Name (Bengali)",
         }
        widgets = {
            "has_sister_concern": forms.RadioSelect(attrs={"class": "inline"}),
        }
        error_messages = {
            'name_en': {
                'unique': ("Mother Organization Name Already Exists"),
            },
            'name_bn': {
                'unique': ("Mother Organization Already Exists"),
            },

        }