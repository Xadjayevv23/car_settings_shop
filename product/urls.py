from django.urls import path
from .views import ShopView, ProductDetailsView, update_cart

app_name = 'products'

urlpatterns = [
    path('', ShopView.as_view(), name='product'),
    path('<int:pk>/detail/', ProductDetailsView.as_view(), name='product-details'),
    path('<int:pk>/cart/', update_cart, name='add_cart'),
]
