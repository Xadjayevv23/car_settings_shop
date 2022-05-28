from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView
from product.models import ProductModel
from .forms import ContactModelForm


class HomePagesView(TemplateView):
    template_name = 'main/index.html'

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q)
            return qs
        return qs


class ShoppingCartView(TemplateView):
    template_name = 'main/shopping-cart.html'


class ContactView(CreateView):
    form_class = ContactModelForm
    template_name = 'main/contact.html'

    def get_success_url(self):
        return reverse('pages:contact')
