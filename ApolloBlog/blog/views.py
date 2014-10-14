from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Article

def index(request):
	latest_articles = Article.objects.order_by('-created_date')[:5]
	context =  {'latest_articles': latest_articles}
	return render(request, 'blog/index.html', context)

def detail(request, article_id):
	article = Article.objects.get(pk=article_id)
	context = {'article': article}
	return render(request, 'blog/details.html', context)