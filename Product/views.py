import decimal

from django.db.models import Avg
from rest_framework import filters, permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response

from Product.models import Product, ProductRatings
from Product.serializers import ProductRatingSerializer, ProductSerializer


@api_view(["GET"])
def api_overview(request):
    api_urls = {
        "overview/": "API overview",
        "": "Product list",
        "create/": "Create product",
        "update/<int:pk>/": "Update product",
        "delete/<int:pk>/": "Delete product",
        "<int:pk>/": "Get product with id",
        "rate/": "Rating list",
        "rate/create": "Create rating",
        "rate/<int:pk>/": "All rating",
        "rate/list/": "Ratings list",
    }
    return Response(api_urls)


class ListProductAPIView(ListAPIView):
    """This endpoint list all the available products from the database"""

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
    """This endpoint list all the available products from the database"""

    queryset = ProductRatings.objects.all()
    serializer_class = ProductRatingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["product", "user", "rating"]


class CreateProductRatingAPIView(CreateAPIView):
    serializer_class = ProductRatingSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(["GET"])
def get_product_with_id(request, pk):
    serializer = ProductSerializer(Product.objects.get(id=pk), many=False)
    return Response(serializer.data)


@api_view(["GET"])
def product_rating_list(request):
    serializer = ProductRatingSerializer(ProductRatings.objects.all(), many=True)
    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def product_rating(request, pk):
    """
    Retrieve, update or delete a code product_rating.
    """

    if not pk:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    try:
        product = Product.objects.get(pk=pk)
    except ProductRatings.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product_rating_ = ProductRatings.objects.get(product=product, user=request.user)
    if request.method == "GET":
        serializer = ProductRatingSerializer(product_rating_, many=False)
        return Response(serializer.data)

    if request.method == "PUT":
        if not product_rating_:
            product_rating_ = ProductRatings.objects.create(
                product=product, rating=request.get("rating"), user=request.user
            )
        else:
            product_rating_.rating = request.data["rating"]

        product_rating_.save()
        product.rating = decimal.Decimal(
            round(
                ProductRatings.objects.filter(product=product).aggregate(Avg("rating"))[
                    "rating__avg"
                ],
                2,
            )
        )
        product.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    elif request.method == "DELETE":
        if not product_rating_:
            return Response(status=status.HTTP_424_FAILED_DEPENDENCY)

        product_rating_.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
