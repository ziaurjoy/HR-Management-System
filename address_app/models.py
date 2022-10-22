from django.db import models

# Create your models here.


class Divisions(models.Model):
    name_english = models.CharField(max_length=25, null=True,default=None)
    name_bengali = models.CharField(max_length=25,null=True,default=None)
    url = models.CharField(max_length=50, null=True,default=None)
    def __str__(self):
        return str(self.name_english)


class Districts(models.Model):
    name_english = models.CharField(max_length=120,default=None)
    name_bengali = models.CharField(max_length=25,default=None)
    url = models.CharField(max_length=50,default=None)
    division = models.ForeignKey(Divisions, on_delete=models.CASCADE, related_name='distric_division')
    def __str__(self):
        return str(self.name_english)


class Upazila(models.Model):
    name_english = models.CharField(max_length=120)
    name_bengali = models.CharField(max_length=25,default=None)
    district = models.ForeignKey(Districts,on_delete=models.CASCADE, related_name='thana_district')
    url = models.CharField(max_length=50,default=None)
    def __str__(self):
        return str(self.name_english)