from django.db import models
from django.conf import settings

from UserMessages.models import UserMessages

from Gallery.models import Image


# Create your models here.
class UserGroups(models.Model):
    FRIENDS = 'FR'
    GROUPS = 'GR'
    TYPE_GROUP = [
        (FRIENDS, 'Friends'),
        (GROUPS, 'Groups'),

    ]
    name = models.CharField(max_length=150,blank=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    messages = models.ManyToManyField(UserMessages, blank=True)
    avatar = models.ManyToManyField(Image,blank=True)
    type_group = models.CharField(
        max_length=2,
        choices=TYPE_GROUP,
        default=FRIENDS,
    )
    class Meta:
        verbose_name = 'Пользовательская группа'
        verbose_name_plural = 'Пользовательские группы'

    def __str__(self):
        if self.type_group == 'FR':
            return f'{self.id}'
        return f'-{self.id}'