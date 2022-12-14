from django.urls import path

from Product.views import (CreateProductAPIView, CreateProductRatingAPIView,
                           DeleteProductAPIView, ListProductAPIView,
                           ListRatingAPIView, UpdateProductAPIView,
                           get_product_with_id, product_rating_list,
                           product_rating_view)

urlpatterns = [
    path("", ListProductAPIView.as_view(), name="product_list"),
    path("create/", CreateProductAPIView.as_view(), name="create_product"),
    path("update/<int:pk>/", UpdateProductAPIView.as_view(), name="update_product"),
    path("delete/<int:pk>/", DeleteProductAPIView.as_view(), name="delete_product"),
    path("<int:pk>/", get_product_with_id, name="get_product_with_id"),
    path("rate/", ListRatingAPIView.as_view(), name="rating_list"),
    path("rate/create", CreateProductRatingAPIView.as_view(), name="create_rating"),
    path("rate/<int:pk>/", product_rating_view, name="all_rating"),
    path("rate/list/", product_rating_list, name="ratings_list"),
]
