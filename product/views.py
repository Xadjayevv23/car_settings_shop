from django.shortcuts import render
from .models import ProductModel
from django.views.generic import ListView, DetailView


class ShopView(ListView):
    model = ProductModel
    template_name = 'main/shop.html'


class ProductDetailsView(DetailView):
    model = ProductModel
    template_name = 'main/product-details.html'
