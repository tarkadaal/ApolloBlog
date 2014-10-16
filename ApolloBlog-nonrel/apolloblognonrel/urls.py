from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth import views as authviews
from apolloblognonrel import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    # Examples:
    # url(r'^$', 'apolloblognonrel.views.home', name='home'),
    # url(r'^apolloblognonrel/', include('apolloblognonrel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', authviews.login, name='login'),
    url(r'^accounts/logout/$', authviews.logout, name='logout'),
)
