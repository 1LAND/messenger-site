from django.db import models
from django.conf import settings

# Create your models here.
class UserMessages(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Пользовательское сообщение'
        verbose_name_plural = 'Пользовательские сообщения'

    def __str__(self):
        return f'{self.id}'