from django.db import models
from PIL import Image
import numpy as np
# Create your models here.
class FloorImage(models.Model):
    username=models.CharField(max_length=100 ,blank=False,default="")
    name = models.CharField(max_length=50,blank=True,default="")
    image = models.ImageField(upload_to='uploads/')

class User(models.Model):
    username=models.CharField(max_length=100)
    data=models.JSONField(null=True,blank=True)
    

