from django.db import models
from django.contrib.auth.models import User

  

# Create your models here.
	

class Services(models.Model):
    services_id = models.AutoField(primary_key=True)
    services_title = models.CharField(max_length=50)
    services_description = models.CharField(max_length=100)
    services_contact = models.CharField(max_length=20)
    services_img = models.CharField(max_length=100)

