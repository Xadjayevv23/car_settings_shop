from django import template
from django.db.models import Sum
from product.models import *

register = template.Library()


@register.simple_tag
def get_cart_info(request):
    cart = request.session.get('cart', [])
    if not cart:
        return 0, 0.0

    return len(cart), ProductModel.get_cart_info(cart).aggregate(Sum('real_price'))['real_price__sum']


@register.filter
def is_cart(request, product):
    return product.pk in request.session.get('cart')