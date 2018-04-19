from django.db import models
from userprofile.models import MyUser
from django.utils import timezone
import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Region(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

class Metro(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Станция метро'
        verbose_name_plural = 'Станции метро'


class Ad(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регион')
    metro = models.ForeignKey(Metro, on_delete=models.CASCADE, verbose_name='Метро')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    desc = models.TextField(max_length=1000, verbose_name='Описание')
    pub_date = models.DateTimeField(auto_now_add=True)
    lookups = models.IntegerField(default=0, verbose_name='Видели')
    is_paid = models.BooleanField(default=False, verbose_name='Сделать вип')
    image = models.ImageField(default='default.jpg', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title
    @property
    def name(self):
        return self.user.first_name
    @property
    def phone_number(self):
        return self.user.email
    @property
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    @property
    def publishing_date(self):
        if self.was_published_recently:
            return 'Сегодня'
        else:
            pd = self.pub_date
            return pd.date()

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
