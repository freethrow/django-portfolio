from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from cloudinary import CloudinaryImage
from autoslug import AutoSlugField

from markdown import markdown
from markdown.extensions import Extension


# Fix the code highlighter
# https://github.com/trentm/django-markdown-deux/issues/20

class EscapeHtml(Extension):
    def extendMarkdown(self, md, md_globals):
        del md.preprocessors['html_block']
        del md.inlinePatterns['html']

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    short = models.TextField()
    cover = models.ForeignKey('Picture', null=True, blank=True, on_delete=models.CASCADE, related_name='cover_img')
    slug = AutoSlugField(populate_from='title')
    is_portfolio = models.BooleanField(default = False)
    weigth = models.IntegerField(default = 1)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):        
        return reverse('article_detail', kwargs={'slug': self.slug})

    def get_cover_url(self):       
        return self.cover.pic.url

    def get_markdown(self):
        return mark_safe(markdown(
            self.body,extensions=[EscapeHtml(),
            'markdown.extensions.nl2br',
            'markdown.extensions.fenced_code']))
        
class Picture(models.Model):

    name = models.CharField(max_length=200)
    pic = models.ImageField(blank = True, null = True,upload_to='images') 
    cloudinaryPic = CloudinaryImage('image')
    article = models.ForeignKey(Article, blank=True, null=True,on_delete=models.CASCADE, related_name='pictures' )

    def __str__(self):
        return self.name

    def get_image_url(self):
        return self.pic.url


    