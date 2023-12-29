from django.urls import path

from . import views

urlpatterns = [
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name = 'product'),
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove_from_cart/<slug:slug>/', views.remove_from_cart, name='remove_from_cart'),
    path('increment/<slug:slug>/', views.increment_cart, name='increment'),
    path('decrement/<slug:slug>/', views.decrement_cart, name='decrement'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('', views.ProductListView.as_view(), name='products'),

]