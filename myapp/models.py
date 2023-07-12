from django.db import models
from PIL import Image
import numpy as np
# Create your models here.
class FloorImage(models.Model):
    name = models.CharField(max_length=50,blank=True,default="")
    image = models.ImageField(upload_to='uploads/')

