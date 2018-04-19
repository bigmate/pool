from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(blank=True,max_length=100, null=True, unique=False)
    balance = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    phone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(default='avatars/avatar.svg', verbose_name='Аватар', upload_to='avatars')
    REQUIRED_FIELDS = ['first_name','username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email