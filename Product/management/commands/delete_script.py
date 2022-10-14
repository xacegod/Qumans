from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from Product.models import Product, ProductRatings


class Command(BaseCommand):
    def handle(self, **options):
        for p in Product.objects.all():
            p.delete()
        for u in User.objects.all():
            u.delete()
        for pr in ProductRatings.objects.all():
            pr.delete()
