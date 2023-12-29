from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from .models import Product
from .cart import Cart

class ProductListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'
    context_object_name = 'product'


class CartView(TemplateView):
    template_name = 'cart.html'


class CheckoutView(TemplateView):
    template_name = 'checkout.html'


def add_to_cart(request, slug):

    product = Product.objects.get(slug=slug)
    print(f'PRODUCT IS {product}')

    cart = Cart(request)
    cart.add(product)

    return render(request, 'cart_menu.html', {'cart': cart})

def increment_cart(request, slug):
    product = Product.objects.get(slug=slug)
    cart = Cart(request)
    

    if request.method == 'POST':
        cart.increment(product)

    return render(request, 'cart.html')

def decrement_cart(request, slug):
    product = Product.objects.get(slug=slug)
    cart = Cart(request)

    if request.method == 'POST':
        cart.decrement(product)

    return render(request, 'cart.html')

def remove_from_cart(request, slug):
    product = Product.objects.get(slug=slug)
    cart = Cart(request)

    cart.remove(product)

    return render(request, 'cart.html')
