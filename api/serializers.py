from rest_framework import serializers

from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):

    cover = serializers.StringRelatedField(many=False)

    class Meta:
        model = Article
        fields = ('title','body','short','cover')