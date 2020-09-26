from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

class Item(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    short = models.TextField()
    cover = models.ImageField(blank = True, null = True, upload_to='cover')
    publicUrl = models.CharField(max_length=255, null=True, blank=True)
    slug = AutoSlugField(populate_from='title')

    def get_absolute_url(self):
        return reverse('portfolio_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Picture(models.Model):
    name = models.CharField(max_length=200)
    pic = models.ImageField(blank = True, null = True,upload_to='portfolio')
    item = models.ForeignKey(Item, null=True, blank = True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name