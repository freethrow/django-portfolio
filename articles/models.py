from django.db import models
from django.urls import reverse
from cloudinary import CloudinaryImage
from autoslug import AutoSlugField

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    short = models.TextField()
    cover = models.ForeignKey('Picture', null=True, blank=True, on_delete=models.CASCADE, related_name='cover_img')
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):        
        return reverse('article_detail', kwargs={'slug': self.slug})
        
class Picture(models.Model):

    name = models.CharField(max_length=200)
    pic = models.ImageField(blank = True, null = True,upload_to='images') 
    cloudinaryPic = CloudinaryImage('image')

    def __str__(self):
        return self.name
    