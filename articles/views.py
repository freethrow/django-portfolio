from django.views.generic import TemplateView, ListView
from .models import Article

class HomePageView(TemplateView):
    
    template_name = 'home.html'

class ArticleListView(ListView):

    model = Article
    template_name = 'articles.html'