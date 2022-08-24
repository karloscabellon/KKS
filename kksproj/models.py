from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class uploadImg(models.Model):
    caption=models.CharField(max_length=100 ,default='UPLOADED IMAGE')
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    def __str__(self):
        return self.caption