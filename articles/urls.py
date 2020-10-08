from django.urls import path
from .views import HomePageView, ArticleListView
from .views import ArticleDetailView, PortfolioListView, AboutPageView, homePage2

urlpatterns = [
    #path('',HomePageView.as_view(), name='home'),
    path('',homePage2, name='home'),
    path('about/',AboutPageView.as_view(), name='about'),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio'),
    path('articles/<slug:slug>', ArticleDetailView.as_view(), name='article_detail'),  
   ]