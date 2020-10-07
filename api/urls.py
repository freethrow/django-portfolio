from django.urls import path

from .views import ArticleAPIView, PortfolioAPIView

urlpatterns = [
    path('articles/',ArticleAPIView.as_view()),
    path('portfolio/',PortfolioAPIView.as_view()),
]