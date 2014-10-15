from django.conf.urls.defaults import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^compose[/]*$', views.compose, name='compose'),
    url(r'^create[/]*$', views.create, name='create'),
    url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),
    url(r'^edit/(?P<article_id>\d+)[/]*$', views.edit, name='edit'),
    url(r'^delete/(?P<article_id>\d+)[/]*$', views.delete, name='delete'),
    url(r'^commit_edit[/]*$', views.commit_edit, name='commit_edit'),
    url(r'^commit_delete[/]*$', views.commit_delete, name='commit_delete'),
)