from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from blog.models import Article

def index(request):
	latest_articles = Article.objects.order_by('-created_date')[:5]
	context =  {'latest_articles': latest_articles}
	return render(request, 'blog/index.html', context)

def detail(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	context  = {'article': article}
	return render(request, 'blog/details.html', context)