from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	url(r'^henkilot_huoneisiin/', include('wad_django.henkilot_huoneisiin.urls')),
	url(r'^elokuvat_ja_genret/', include('wad_django.elokuvat_ja_genret.urls')),
    # Examples:
    # url(r'^$', 'wad_django.views.home', name='home'),
    # url(r'^wad_django/', include('wad_django.foo.urls')),
)
