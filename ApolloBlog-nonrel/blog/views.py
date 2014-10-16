import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from blog.models import Article

def index(request):
	latest_articles = Article.objects.order_by('-created_date')[:15]
	context =  {'latest_articles': latest_articles}
	return render(request, 'blog/index.html', context)


def detail(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	context  = {'article': article}
	return render(request, 'blog/details.html', context)

@login_required
def compose(request):
	return render(request, 'blog/compose.html')

@login_required
def create(request):
	new_article = Article(
		title=request.POST['title'],
		body=request.POST['body'],
		created_date=datetime.datetime.now())
	new_article.save()
	return HttpResponseRedirect(reverse('blog:detail', args=(new_article.id, )))

@login_required
def edit(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	context = {'article': article }
	return render(request, 'blog/edit.html', context)

def commit_edit(request):
	article = get_object_or_404(Article, pk= request.POST['id'])
	article.title = request.POST['title']
	article.body = request.POST['body']
	article.save()
	return HttpResponseRedirect(reverse('blog:detail', args=(article.id, )))

@login_required
def delete(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	context = {'article': article }
	return render(request, 'blog/delete.html', context)
	
@login_required
def commit_delete(request):
	article = get_object_or_404(Article, pk=request.POST['id'])
	article.delete()
	return HttpResponseRedirect(reverse('blog:index'))