from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	url(r'^henkilot_huoneisiin/', include('wad_django.henkilot_huoneisiin.urls')),
    # Examples:
    # url(r'^$', 'wad_django.views.home', name='home'),
    # url(r'^wad_django/', include('wad_django.foo.urls')),
)
