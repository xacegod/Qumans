from rest_framework import filters, permissions
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, UpdateAPIView)

from Product.models import Product
from Product.serializers import ProductSerializer


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
