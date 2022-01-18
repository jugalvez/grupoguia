#encoding:utf-8
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Product, Purchase
from django.db.models import Q
import json


def home(request):
    products = Product.objects.filter(quantity__gt = 0)

    response = {
        'products': products
    }

    return render(request, 'products/home.html', response)


def details(request, slug):
    product = Product.objects.get(slug = slug)
    similar_products = Product.objects.filter(~Q(id=product.id)).order_by('?')
    similar_products_len = similar_products.count()

    similar_products = similar_products[0:3] if similar_products.count() > 4 else similar_products

    response = {
        'product': product,
        'similar_products': similar_products
    }

    return render(request, 'products/details.html', response)


def cart(request):
    return render(request, 'products/cart.html')


def checkout(request):
    return render(request, 'products/checkout.html')


def payment(request):
    resultados = []
    data = { 'message': 'Error', 'status': 400 }

    if request.method == 'GET':
        if request.is_ajax():
            data = request.GET.getlist('data')[0]
            data = json.loads(data)

            for item in data:
                product = Product.objects.get(id=item['id'])
                
                # Update Product
                removeQuantities = product.quantity - item['quantity']
                removeCondition = product.quantity > item['quantity']
                product.quantity = removeQuantities if removeCondition else 0

                purchase = Purchase(
                                product = product, 
                                price = item['price'],
                                quantity = item['quantity'] if removeCondition else product.quantity,
                                total = item['price'] * item['quantity']
                            )
                
                product.save()
                purchase.save()
                
                data = { 'message': 'Purchase completed', 'status': 200 }

    data = json.dumps(data)
    return HttpResponse(data, content_type="application/json")