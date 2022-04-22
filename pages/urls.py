from django.urls import path
from .views import HomePagesView, ContactView

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('', HomePagesView.as_view(), name='home')
]