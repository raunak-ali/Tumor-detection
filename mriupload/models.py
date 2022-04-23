from django.db import models

# Create your models here.
class POST(models.Model):
    MRI_IMAGE=models.ImageField(upload_to='imagess/')
    def __str__(self):
        return self.MRI_IMAGE
    