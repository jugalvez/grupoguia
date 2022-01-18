from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('details/<slug:slug>/', views.details, name='details'),
  path('cart/', views.cart, name='cart'),
  path('checkout/', views.checkout, name='checkout'),
  path('checkout/payment', views.payment, name='payment'),
]
