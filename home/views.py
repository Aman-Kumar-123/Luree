from django.shortcuts import render
import json
# from django.views.generic.base import TemplateView
from .models import Product,ProductSize

# Create your views here.

def Home(request):
    products = Product.objects.all()

    # Create a single dictionary to hold all product size data, keyed by product ID
    all_product_size_data = {}
    for product in products:
        # Fetch all related ProductSize objects for the current product
        product_sizes = ProductSize.objects.filter(product=product).order_by('size')
        
        # Create a list of dictionaries containing size and quantity information
        size_data = []
        for size_instance in product_sizes:
            size_data.append({
                'size': size_instance.size,
                'quantity': size_instance.quantity
            })
        
        # Store the size data for this product using its ID as the key
        # The ID is converted to a string to ensure it's a valid JSON key
        all_product_size_data[str(product.id)] = size_data

    # Prepare the context to pass to the template
    context = {
        'products': products,
        'all_product_size_data': all_product_size_data,
    }

    # Render the index.html template with the prepared context
    return render(request, 'index.html', context)

def Cart(request):
    return render(request,'shopping-cart.html')

def About(request):
    return render(request,'about.html')

