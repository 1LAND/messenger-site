from django.db import models


def upload_to(instance, filename):
    return '/'.join(['images', str(instance.name), filename])
# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=100)
    file = models.ImageField(upload_to=upload_to, blank=True, null=True)