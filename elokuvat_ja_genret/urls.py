from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('wad_django.elokuvat_ja_genret.views',
	url(r'^$', 'index'),
	url(r'^genret_elokuvaan/(\d+)/$', 'genret_elokuvaan'),
	url(r'^genre/(\d+)/$', 'listaa_genre'),

	url(r'lisaa_genre$', 'lisaa_genre'),
	url(r'lisaa_elokuva', 'lisaa_elokuva'),
)
