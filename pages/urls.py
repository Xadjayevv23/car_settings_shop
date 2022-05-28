from django.urls import path
from .views import HomePagesView, ContactView, ShoppingCartView

app_name = 'pages'

urlpatterns = [
    path('shopping-cart/', ShoppingCartView.as_view(), name='shopping-cart'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('', HomePagesView.as_view(), name='home')
]