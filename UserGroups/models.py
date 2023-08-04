from django.db import models
from django.conf import settings

from UserMessages.models import UserMessages

# from Gallery.models import Img


# Create your models here.
class UserGroups(models.Model):
    name = models.CharField(max_length=150,blank=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    messages = models.ManyToManyField(UserMessages, blank=True)
    # avatar = models.ManyToManyField(Img,blank=True)
    type_groups = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Пользовательская группа'
        verbose_name_plural = 'Пользовательские группы'

    def __str__(self):
        if self.type_groups:
            return f'{self.id}'
        return f'-{self.id}'