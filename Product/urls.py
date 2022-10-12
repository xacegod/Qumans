from django.urls import path

from Product.views import (
    CreateProductAPIView,
    CreateProductRatingAPIView,
    DeleteProductAPIView,
    DeleteProductRatingAPIView,
    ListProductAPIView,
    ListRatingAPIView,
    UpdateProductAPIView,
    UpdateProductRatingAPIView,
)

urlpatterns = [
    path("", ListProductAPIView.as_view(), name="product_list"),
    path("create/", CreateProductAPIView.as_view(), name="product_create"),
    path("update/<int:pk>/", UpdateProductAPIView.as_view(), name="update_product"),
    path("delete/<int:pk>/", DeleteProductAPIView.as_view(), name="delete_product"),
    path("rate/", ListRatingAPIView.as_view(), name="rating_list"),
    path("rate/create", CreateProductRatingAPIView.as_view(), name="create_rating"),
    path("rate/update", UpdateProductRatingAPIView.as_view(), name="update_rating"),
    path("rate/delete", DeleteProductRatingAPIView.as_view(), name="delete_rating"),
]
