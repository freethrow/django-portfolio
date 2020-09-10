from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    short = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):        
        return reverse('article_detail', kwargs={'pk': self.pk})