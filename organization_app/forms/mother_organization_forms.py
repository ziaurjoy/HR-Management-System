from django import forms
from ..models import mother_organization_models


class MotherOrganizationCreateForms(forms.ModelForm):
    choicess = (
        ('True', 'Yes'),
        ('False', 'No')
    )
    has_sister_concern = forms.ChoiceField(choices=choicess, widget=(forms.RadioSelect(attrs={'class': 'inline'})))
    class Meta:
        model = mother_organization_models.MotherOrganizations
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
    choicess = (
        ('True', 'Yes'),
        ('False', 'No')
    )
    has_sister_concern = forms.ChoiceField(choices=choicess, widget=(forms.RadioSelect(attrs={'class': 'inline'})))
    class Meta:
        model = mother_organization_models.MotherOrganizations
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