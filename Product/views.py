from django.db.models import Avg
from rest_framework import filters, permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, UpdateAPIView)
from rest_framework.response import Response

from Product.models import Product, ProductRatings
from Product.serializers import ProductRatingSerializer, ProductSerializer


class ListProductAPIView(ListAPIView):
    """This endpoint lists all the available products from the database"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "id", "price", "updated_at", "rating"]
    ordering_fields = ["name", "id", "price", "updated_at", "rating"]


class CreateProductAPIView(CreateAPIView):
    """This endpoint allows for creation of a product"""

    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateProductAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific product by passing in the id of the product to update"""

    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeleteProductAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific product from the database"""

    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListRatingAPIView(ListAPIView):
    """This endpoint lists ratings for all the available products from the database"""

    queryset = ProductRatings.objects.all()
    serializer_class = ProductRatingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["product", "user", "rating"]


class CreateProductRatingAPIView(CreateAPIView):
    """This endpoint is used for rating a product"""
    serializer_class = ProductRatingSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(["GET"])
def get_product_with_id(request, pk):
    """
    This endpoint retrieves a specific product by id.
    """
    serializer = ProductSerializer(Product.objects.get(id=pk), many=False)
    return Response(serializer.data)


@api_view(["GET"])
def product_rating_list(request):
    """
    This endpoint lists saved ratings for all products from the database.
    """
    serializer = ProductRatingSerializer(ProductRatings.objects.all(), many=True)
    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def product_rating_view(request, pk):
    """
    Retrieve, update or delete product_rating depending on the method.
    """

    if not pk:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    try:
        product = Product.objects.get(pk=pk)
    except ProductRatings.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product_rating = ProductRatings.objects.get(product=product, user=request.user)
    if request.method == "GET":
        serializer = ProductRatingSerializer(product_rating, many=False)
        return Response(serializer.data)

    if request.method == "PUT":
        if not product_rating:
            product_rating = ProductRatings.objects.create(
                product=product, rating=request.get("rating"), user=request.user
            )
        else:
            product_rating.rating = request.data["rating"]

        product_rating.save()
        product.rating = round(
            ProductRatings.objects.filter(product=product).aggregate(Avg("rating"))[
                "rating__avg"
            ],
            2,
        )
        product.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    elif request.method == "DELETE":
        if not product_rating:
            return Response(status=status.HTTP_424_FAILED_DEPENDENCY)

        product_rating.delete()

        product.rating = round(
            ProductRatings.objects.filter(product=product).aggregate(Avg("rating"))[
                "rating__avg"
            ],
            2,
        )
        product.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
