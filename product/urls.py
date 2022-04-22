from django.urls import path
from .views import ShopView, ProductDetailsView

app_name = 'products'

urlpatterns = [
    path('', ShopView.as_view(), name='product'),
    path('<int:pk>/detail/', ProductDetailsView.as_view(), name='product-details')
]
