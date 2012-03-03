from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('wad_django.henkilot_huoneisiin.views',
	url(r'^$', 'index'),
	url(r'lisaa_huone$', 'lisaa_huone'),
	url(r'lisaa_henkilo', 'lisaa_henkilo'),
	url(r'poista_huone/(\d+)/$', 'poista_huone'),
	url(r'poista_henkilo/(\d+)/$', 'poista_henkilo'),
)
