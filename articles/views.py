from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from .models import Article
from portfolio.models import Item, Picture



class HomePageView(TemplateView):
    
    template_name = 'home.html'

class ArticleListView(ListView):

    model = Article
    template_name = 'articles.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'single_article.html'