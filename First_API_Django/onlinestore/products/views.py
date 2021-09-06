from django.http import JsonResponse, response

# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

from .models import Product, Manufacturer
# Create your views here.

def product_list(req):
    products = Product.objects.all()

    # This is just gonna get pk and name 
    # data = {"products": list(products.values("pk", "name"))}
    data = {"products": list(products.values())}
    response = JsonResponse(data)
    return response

def product_detail(req, pk):
    try:
        product = Product.objects.get(pk = pk)

        # All these fields are from models
        data = {
            "product":{
                "name": product.name,
                "manufacturer": product.manufacturer.name,
                "description": product.description,
                "photo": product.photo.url,
                "price": product.price,
                "shipping_cost": product.shipping_cost,
                "quantity": product.quantity
            }
        }
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error":{
                "code": 404,
                "message": "Wand not found!"
            }
        },
        status = 404)
    
    return response

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"


# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"
