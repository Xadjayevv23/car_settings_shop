from django.urls import path
from .views import HomePagesView

app_name = 'pages'

urlpatterns = [
    path('', HomePagesView.as_view(), name='home')
]