from django.template.context_processors import request
from rest_framework import filters, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from Product.models import Product, ProductRatings
from Product.serializers import ProductRatingSerializer, ProductSerializer


class ListProductAPIView(ListAPIView):
    """This endpoint list all of the available products from the database"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "id", "price", "updated_at", "rating"]


class CreateProductAPIView(CreateAPIView):
    """This endpoint allows for creation of a product"""

    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateProductAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific product by passing in the id of the product to update"""

    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeleteProductAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Product from the database"""

    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListRatingAPIView(ListAPIView):
    """This endpoint list all of the available products from the database"""

    queryset = ProductRatings.objects.all()
    serializer_class = ProductRatingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["product", "user", "rating"]


# class CreateProductRatingAPIView(CreateAPIView):
#     """This endpoint allows for creation of a product"""
#
#     serializer_class = ProductRatingSerializer
#     permission_classes = [permissions.IsAuthenticated]


class CreateProductRatingAPIView(CreateAPIView):
    serializer_class = ProductRatingSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateProductRatingAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific product by passing in the id of the product to update"""

    queryset = ProductRatings.objects.all()
    serializer_class = ProductRatingSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeleteProductRatingAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific ProductRating from the database"""

    serializer_class = ProductRatingSerializer
    permission_classes = [permissions.IsAuthenticated]
