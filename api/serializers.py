from rest_framework import serializers

from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):

    cover_url = serializers.CharField(source='get_cover_url', read_only=True)

    
    class Meta:
        model = Article
        fields = ('title','body','short','cover_url','is_portfolio')