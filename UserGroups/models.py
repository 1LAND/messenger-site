from django.db import models
from django.conf import settings

from UserMessages.models import UserMessages

# Create your models here.
class UserGroups(models.Model):
    name = models.CharField(max_length=150)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    messages = models.ManyToManyField(UserMessages, blank=True)
    type_groups = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Пользовательская группа'
        verbose_name_plural = 'Пользовательские группы'

    def __str__(self):
        if self.type_groups:
            return f'{self.id}'
        return f'-{self.id}'

class AdminUserGroup(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    group = models.ForeignKey(UserGroups, on_delete=models.CASCADE)    