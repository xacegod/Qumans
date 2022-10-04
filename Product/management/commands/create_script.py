from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from Product.models import Product
import random
import decimal

class Command(BaseCommand):
    def handle(self, **options):
        if not User.objects.get(username="super"):
            user = User.objects.create(
                username="super", email="super@user.com", password=make_password("tesT123")
            )
            user.is_superuser = True
            user.save()

        if not User.objects.get(username = "user1"):
            user1 = User.objects.create(
                username="user1", email="use2r@user.com", password=make_password("tesT123")
            )
            user1.is_superuser = False
            user1.save()

        if not User.objects.get(username="user2"):
            user2 = User.objects.create(
                username="user2", email="user2@user.com", password=make_password("tesT123")
            )
            user2.is_superuser = False
            user2.save()

        for i in range(0, 20):
            product = Product.objects.create(
                id=Product.objects.latest("id").id+1 if Product.objects.latest("id").id else 0,
                name="Product #%s" % (Product.objects.latest("id").id+1 if Product.objects.latest("id").id else 0),
                price=decimal.Decimal(random.randrange(100, 500000))/100,
                rating=decimal.Decimal(random.randrange(100, 500))/100,
                updated_at=datetime.date(datetime.now()),
            )
            product.save()
