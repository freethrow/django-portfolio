from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from django.views.generic.detail import DetailView

from .models import Item, Picture

class ItemListView(ListView):

    model = Item
    template_name = 'portfolio_items.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'portfolio_item.html'
