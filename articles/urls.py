from django.urls import path
from .views import HomePageView, ArticleListView, ArticleDetailView

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/<slug:slug>', ArticleDetailView.as_view(), name='article_detail'),  
   ]