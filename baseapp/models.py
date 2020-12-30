from django.db import models

# Create your models here.


class PestControl(models.Model):
    custname = models.CharField(max_length=100)
    mobile = models.IntegerField(unique=True)
    type_of_pest = models.CharField(max_length=50)
    location = models.CharField(max_length=300)
    
    def __str__(self):
        return self.custname
