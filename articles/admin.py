from django.contrib import admin
from django import forms
from pagedown.widgets import AdminPagedownWidget

from .models import Article, Picture
# Register your models here.


class ArticleForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Article
        fields = ['title','is_portfolio','short','cover','body','weigth']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    fields = ['title','is_portfolio','short','cover','body','weigth']


admin.site.register(Picture)