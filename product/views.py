from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductModel, CategoryModel, SizeModel, ColorModel
from django.views.generic import ListView, DetailView


class ShopView(ListView):
    model = ProductModel
    template_name = 'main/shop.html'
    paginate_by = 6

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q)
            return qs
        return qs

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ShopView, self, *args, **kwargs).get_context_data()
        context['sizes'] = SizeModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        return context


class ProductDetailsView(DetailView):
    model = ProductModel
    template_name = 'main/product-details.html'


def update_cart(request, pk):
    product = get_object_or_404(ProductModel.objects.all().filter(id=pk))
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)

    request.session['cart'] = cart

    return redirect(request.GET.get('next', '/'))


class CartListView(ListView):
    template_name = 'main/shopping-cart.html'

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        ProductModel.get_cart_info(cart)
