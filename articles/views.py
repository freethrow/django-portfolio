from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .forms import ContactForm

from .models import Article, Picture


class HomePageView(ListView):
    model = Article
    queryset = Article.objects.all() 
    form_class = ContactForm   
    template_name = 'home.html'
    

class AboutPageView(TemplateView):    
    template_name = 'about.html'

class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter(is_portfolio=False)
    template_name = 'articles.html'

class PortfolioListView(ListView):
    model = Article
    queryset = Article.objects.filter(is_portfolio=True)
    template_name = 'articles.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'single_article.html'

# function based view for the homepage
# it has to handle the contact form and display the articles/portfolio
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def homePage2(request):
    
    articles = Article.objects.all()

    if request.method == 'GET':
        form = ContactForm()

    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'From the website'
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('about')
    return render(request, "home2.html", {'form': form, 'articles':articles})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')