from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.


def startpage(request):
    # products = [
    #     { 'name': 'Lenovo', 'price': '500', 'discount': True},
    #     {'name': 'Aser', 'price': '600'},
    #     {'name': 'Asus', 'price': '700'},
    #     {'name': 'Samsung', 'price': '900'},
    # ]

    products = Product.objects.all()
    print (products)
    context = {
        'name': "alex",
        'surname': "ben",
        'products': products
    }
    return render(
        request,
        'main.html',
      )

def starttest(request):
    return HttpResponse('Test response')