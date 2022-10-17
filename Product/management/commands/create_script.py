import random
from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.models import Avg

from Product.models import Product, ProductRatings


class Command(BaseCommand):
    def handle(self, **options):
        user, created = User.objects.get_or_create(
            username="super",
            email="super@user.com",
            password=make_password("tesT123"),
        )

        user1, created = User.objects.get_or_create(
            username="user1",
            email="use2r@user.com",
            password=make_password("tesT123"),
        )

        user2, created = User.objects.get_or_create(
            username="user2",
            email="user2@user.com",
            password=make_password("tesT123"),
        )

        Product.objects.get_or_create(
            id=1,
            name="Product #1",
            price=random.randrange(100, 500000) / 100,
            rating=0,
            updated_at=datetime.date(datetime.now()),
        )

        for i in range(0, 20):
            product = Product.objects.create(
                id=Product.objects.latest("id").id + 1,
                name="Product #%s" % (Product.objects.latest("id").id + 1),
                price=random.randrange(100, 500000) / 100,
                rating=0,
                updated_at=None,
            )
            product.save()

            ProductRatings.objects.create(
                product=product,
                user=user,
                rating=random.randrange(100, 500) / 100,
            ).save()
            ProductRatings.objects.create(
                product=product,
                user=user1,
                rating=random.randrange(100, 500) / 100,
            ).save()
            ProductRatings.objects.create(
                product=product,
                user=user2,
                rating=random.randrange(100, 500) / 100,
            ).save()

            product.rating = round(
                ProductRatings.objects.filter(product=product).aggregate(Avg("rating"))[
                    "rating__avg"
                ],
                2,
            )

            product.save()
