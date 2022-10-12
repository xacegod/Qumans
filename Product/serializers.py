import decimal

from django.db.models import Avg
from rest_framework import serializers

from Product.models import Product, ProductRatings


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRatings
        fields = ["product", "rating", "user"]

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        p = validated_data.get("product")
        if pr := ProductRatings.objects.filter(
            product=p, user=validated_data.get("user")
        ).first():
            pr.rating = validated_data.get("rating")
        else:
            pr = ProductRatings.objects.create(
                product=p,
                user=validated_data.get("user"),
                rating=validated_data.get("rating"),
            )
        pr.save()
        p.rating = decimal.Decimal(
            round(
                ProductRatings.objects.filter(product=p).aggregate(Avg("rating"))[
                    "rating__avg"
                ],
                2,
            )
        )
        p.save()
        return validated_data

    def update(self, instance, validated_data):
        print(instance, validated_data)
        return validated_data
