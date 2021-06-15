from django.db import models
from django.conf import settings
import os
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'Profil użytkownika {self.user.username}.'

    def get_absolute_image(self):
        return os.path.join('/media/', self.photo.name)
