from django.contrib.auth.models import AbstractUser
from django.db import models
from . import choices
from organization_app.models import organization_models
class Users(AbstractUser):
    user_type = models.CharField(choices=choices.user_type,blank=True,null=True, max_length=100)
    mother_organization = models.ForeignKey(organization_models.MotherOrganizations, related_name='user_mother_organization',blank=True,null=True, on_delete=models.PROTECT)
    sister_organization = models.ForeignKey(organization_models.SisterOrganizations, related_name='user_sister_organization',blank=True,null=True, on_delete=models.PROTECT)
    branch = models.ForeignKey(organization_models.Branches, related_name='user_branch',blank=True,null=True, on_delete=models.PROTECT)
    
