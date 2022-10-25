from django.db import models
from rbac_app.models import users_models
from organization_app.models import organization_models

class UserPermissions(models.Model):
    user=models.ForeignKey(users_models.Users, on_delete=models.PROTECT, related_name='permission_user',default=None)
    permission = models.CharField(max_length=50)
    mother_organization = models.ForeignKey(organization_models.MotherOrganizations, related_name='permission_mother_organization', on_delete=models.PROTECT)
    sister_organization = models.ForeignKey(organization_models.SisterOrganizations, related_name='permission_sister_organization', on_delete=models.PROTECT)
    branch = models.ForeignKey(organization_models.Branches, related_name='permission_branch', on_delete=models.PROTECT)
    # class Meta:
    #     unique_together = ('user','permission')

