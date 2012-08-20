from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin
import deejango

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', 'deejango.main.views.index'),
    url(r'^beer/$', 'deejango.beer.views.beers_all'),
    url(r'^test_area/$', 'deejango.main.views.test_area'),
    url(r'^test_area_two/$', 'deejango.pages.views.home_page'),
    url(r'^beer/(?P<beerslug>.*)/$', 'deejango.beer.views.specific_beer'),
    url(r'^breweries/(?P<breweryslug>.*)/$', 'deejango.beer.views.specific_brewery'),
    url(r'^register/$', 'deejango.drinker.views.drinker_registration'),
    url(r'^login/$', 'deejango.drinker.views.login_request'),
    url(r'^logout/$', 'deejango.drinker.views.logout_request'),
    url(r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^direct/$', direct_to_template, {'template': 'direct.html', 'extra_context': {'showDirect': True}}),
    url(r'^profile/$', 'deejango.drinker.views.profile'),
    url(r'^blog/$', 'deejango.blog.views.posts_all'),
    url(r'^blog/(?P<postslug>.*)/$', 'deejango.blog.views.specific_post'),

)
