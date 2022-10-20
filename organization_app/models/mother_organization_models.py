
from django.db import models

class MotherOrganizations(models.Model):
    name_en = models.CharField(max_length=100)
    name_bn = models.CharField(max_length=100)
    number_of_user = models.IntegerField(default=0)
    has_sister_concern = models.BooleanField(default=False)

    def __str__(self):
        return self.name_en