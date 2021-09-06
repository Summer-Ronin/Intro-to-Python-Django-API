from django.urls import path
# from .views import ProductListView, ProductDetailView
from .views import product_list, product_detail

# Don't uppercase the urlpatterns
# urlpatterns = [
#     path("", ProductListView.as_view(), name="product-list"),
#     # Pass product primary key to the view, pk is primary key
#     path("products/<int:pk>", ProductDetailView.as_view(), name="product-detail")
# ]

urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>", product_detail, name="product-detail")
]
