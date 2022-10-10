from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

"""
 ○ id (primary, integer)
 ○ name (required, string, unique)
 ○ price (required) # no information about type
 ○ rating (required, float, min 0; max 5)
 ○ updated_at (optional, date)
"""


class Product(models.Model):
    id = models.IntegerField(blank=False, unique=True, primary_key=True, null=False)
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    price = models.DecimalField(
        decimal_places=2,
        validators=[MinValueValidator(0)],
        max_digits=20,
        null=False,
        blank=False,
    )
    rating = models.DecimalField(
        max_digits=3,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        decimal_places=2,
        help_text="Rating - can go from 1 to 5.",
        null=False,
        blank=False,
    )
    updated_at = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return "%s - %s - $%s Rated: %s" % (self.id, self.name, self.price, self.rating)
