from django.urls import path
# from .views import ProductListView, ProductDetailView
from .views import manufacturer_list, product_list, product_detail, manufacturer_detail, manufacturer_list_active

# Don't uppercase the urlpatterns
# urlpatterns = [
#     path("", ProductListView.as_view(), name="product-list"),
#     # Pass product primary key to the view, pk is primary key
#     path("products/<int:pk>", ProductDetailView.as_view(), name="product-detail")
# ]

urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>", product_detail, name="product-detail"),

    path("manufacturers/", manufacturer_list, name="manufacturer-list"),
    path("manufacturers/<int:pk>", manufacturer_detail, name="manufacturer-detail"),

    path("manufacturers_active/", manufacturer_list_active, name="manufacturer-list-active")
]
