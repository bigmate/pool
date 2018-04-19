from .models import Category, Ad, Region, Metro
from userprofile.models import MyUser
from faker import Faker
fake = Faker()
import random

for i in range(50):
    item, flag = MyUser.objects.get_or_create(
        email=fake.email(),
        username=fake.user_name(),
        first_name=fake.name(),
        balance=fake.random_int(min=200, max=300),
        phone=fake.phone_number()
    )
    item.set_password(fake.password(length=10))
    item.save()

CHOICES_CATEGORY = Category.objects.all()
CHOICES_REGION = Region.objects.all()
CHOICES_METRO = Metro.objects.all()
CHOICES_USER = MyUser.objects.all()
CHOICES_TITLE_LEN = list(range(100, 200))
CHOICES_DESC_LEN  = list(range(500, 900))

def generate():
    for i in range(100):
        category = random.choice(CHOICES_CATEGORY)
        region = random.choice(CHOICES_REGION)
        metro = random.choice(CHOICES_METRO)
        user = random.choice(CHOICES_USER)
        title_len = random.choice(CHOICES_TITLE_LEN)
        desc_len = random.choice(CHOICES_DESC_LEN)
        is_paid = random.choice((True, False))
        Ad.objects.get_or_create(
            user=user,
            title=fake.text(title_len),
            desc=fake.text(desc_len),
            region=region,
            metro=metro,
            category=category,
            is_paid=is_paid
        )