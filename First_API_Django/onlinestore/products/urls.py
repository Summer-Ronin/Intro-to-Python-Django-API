from django.urls import path
from django.urls.resolvers import URLPattern
from .views import ProductListView, ProductDetailView

# Don't uppercase the urlpatterns
urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    # Pass product primary key to the view, pk is primary key
    path("products/<int:pk>", ProductDetailView.as_view(), name="product-detail")
]
