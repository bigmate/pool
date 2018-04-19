from django.contrib import admin
from .models import Ad, Category, Region, Metro
# Register your models here.
admin.site.register(Region)
admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(Metro)