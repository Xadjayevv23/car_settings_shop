from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView
from .forms import ContactModelForm


class HomePagesView(TemplateView):
    template_name = 'main/index.html'

    def get_queryset(self):
        pass


class ContactView(CreateView):
    form_class = ContactModelForm
    template_name = 'main/contact.html'

    def get_success_url(self):
        return reverse('pages:contact')
