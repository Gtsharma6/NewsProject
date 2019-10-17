from django.db import models

# Create your models here.

class AddUser(models.Model):
   
    Email = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    
    Active = models.BooleanField(blank=True,default=False)
