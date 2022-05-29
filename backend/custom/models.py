from django.db import models

# Create your models here.
class Convert(models.Model):
    name = models.CharField(max_length=50)
    convert_Main_Img = models.ImageField(upload_to='images/')

class Audio(models.Model):
    # name = models.CharField(max_length=50)
    convert_audio = models.FileField(upload_to='audio/')