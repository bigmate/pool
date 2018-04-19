from django.db import models
from userprofile.models import MyUser
from django.utils import timezone
import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='media/icons')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Region(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

class Metro(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Metro station'
        verbose_name_plural = 'Metro stations'


class Ad(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region')
    metro = models.ForeignKey(Metro, on_delete=models.CASCADE, verbose_name='Meto station')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categories')
    title = models.CharField(max_length=255, verbose_name='Title')
    desc = models.TextField(max_length=1000, verbose_name='Description')
    pub_date = models.DateTimeField(auto_now_add=True)
    lookups = models.IntegerField(default=0, verbose_name='Seen')
    is_paid = models.BooleanField(default=False, verbose_name='Mark as VIP')
    image = models.ImageField(default='default.jpg', blank=True, verbose_name='Photo')

    def __str__(self):
        return self.title

    @property
    def name(self):
        return self.user.first_name
    @property
    def phone_number(self):
        return self.user.phone
    @property
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    @property
    def publishing_date(self):
        if self.was_published_recently:
            return 'Today'
        else:
            pd = self.pub_date
            return pd.date()

    class Meta:
        verbose_name = 'Ad'
        verbose_name_plural = 'Ads'
