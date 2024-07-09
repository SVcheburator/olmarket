from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Category(models.Model):
    name = models.CharField(null=False)
    icon = CloudinaryField('image', null=True, blank=True)

    def _str_(self):
        return f"{self.name}"