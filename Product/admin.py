from django.contrib import admin

from .models import Product, ProductRatings


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ["name", "id", "price", "updated_at", "rating"]


@admin.register(ProductRatings)
class RatingAdmin(admin.ModelAdmin):
    pass
