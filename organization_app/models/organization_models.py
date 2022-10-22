
from django.db import models

class MotherOrganizations(models.Model):
    name_en = models.CharField(max_length=100)
    name_bn = models.CharField(max_length=100)
    number_of_user = models.IntegerField(default=0)
    has_sister_concern = models.BooleanField(default=False)
    def __str__(self):
        return self.name_en



class SisterOrganizations(models.Model):
    mother_organization = models.ForeignKey('organization_app.MotherOrganizations', related_name='sister_mother_organization', on_delete=models.PROTECT,null=True)
    name_english = models.CharField(max_length=100,null=True)
    name_bengali = models.CharField(max_length=100,null=True)
    division = models.ForeignKey('address_app.Divisions', on_delete=models.PROTECT, related_name='sister_organization_division',default=None,null=True)
    district = models.ForeignKey('address_app.Districts', on_delete=models.PROTECT, related_name='sister_organization_districs',default=None,null=True)
    upazila = models.ForeignKey('address_app.Upazila', on_delete=models.CASCADE, related_name='sister_organization_upazila',default=None,null=True)
    address_details = models.CharField(max_length=200,null=True)
    website_address = models.CharField(max_length=200,null=True)
    has_branch_concern = models.BooleanField(default=False)
    def __str__(self):
        return self.name_engalish