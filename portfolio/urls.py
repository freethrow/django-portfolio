from django.urls import path

from .views import ItemListView, ItemDetailView

urlpatterns = [
    path('', ItemListView.as_view(), name='portfolio_list'),
    path('<slug:slug>', ItemDetailView.as_view(), name='portfolio_detail'),
]