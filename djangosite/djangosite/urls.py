from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangosite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','djangosite.views.home',name="home"),
    url(r'^browseCategory','djangosite.views.browseCategory',name="browseCategory"),
    url(r'^browseTag','djangosite.views.browseTag',name="browseTag"),
    url(r'^itemListing','djangosite.views.itemListing',name="itemListing"),
    url(r'^search','djangosite.views.search',name="search"),
    url(r'^shoppingCart','djangosite.views.shoppingCart',name="shoppingCart"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^acc/', include('accountstuff.urls')),
    url(r'^item/', include('itemstuff.urls')),
    url(r'^browse/(?P<category>.+)$', 'itemstuff.views.browseCategory', name="browseCategory"),
)
