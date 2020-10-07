from rest_framework import generics

from articles.models import Article

from .serializers import ArticleSerializer


class ArticleAPIView(generics.ListAPIView):

    queryset = Article.objects.filter(is_portfolio=False)
    serializer_class = ArticleSerializer


class PortfolioAPIView(generics.ListAPIView):

    queryset = Article.objects.filter(is_portfolio=True)
    serializer_class = ArticleSerializer