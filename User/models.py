from django.db import models
from django.contrib.auth.models import PermissionsMixin

from UserGroups.models import UserGroups

from Gallery.models import Image

from django.contrib.auth.models import AbstractUser

# class User(AbstractBaseUser, PermissionsMixin):
#     login = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     avatar = models.ManyToManyField(Image,blank=True)
#     groups = models.ManyToManyField(UserGroups,blank=True)
#     last_singin = models.DateTimeField(auto_now=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'login'
#     REQUIRED_FIELDS = []

#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'

#     def __str__(self):
#         return self.email


class User(AbstractUser):
    groups = models.ManyToManyField(UserGroups,blank=True)
    avatar = models.ManyToManyField(Image,blank=True)
    last_singin = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    def __str__(self):
        return self.username