from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shareanimesub.views.home', name='home'),
    # url(r'^shareanimesub/', include('shareanimesub.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:


    url(r'^projeto/(?P<projeto_id>\d+)/$', 'projetos.views.pagina_projeto'),


    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),

    url(r'^$', 'projetos.views.view_test'),
)

urlpatterns += staticfiles_urlpatterns()
