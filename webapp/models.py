from django.db import models
from django.contrib.auth.models import User

STATUS = [
    ('active',"active"),
    ('inactive',"inactive"),
]

class Building(models.Model):
    name= models.CharField(max_length=50)
    location= models.CharField(max_length=50)
    owner= models.CharField(max_length=50)
    units_count= models.IntegerField()

    def __str__(self):
        return self.name

class Tenant(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField()
    phone= models.CharField(max_length=50)
    next_of_kin= models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TenantBuilding(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL,null=True)
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True)
    checkin_date= models.DateField(null=True, blank=True)
    contract_amount = models.FloatField()
    status = models.CharField(choices=STATUS, default='active',max_length=128)
    


    

    


