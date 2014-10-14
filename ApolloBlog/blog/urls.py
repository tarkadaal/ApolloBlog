from django.conf.urls.defaults import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^compose[/]*$', views.compose, name='compose'),
    url(r'^create[/]*$', views.create, name='create'),
    url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),
)