from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from balance_sheets import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nonprofits.views.home', name='home'),
    # url(r'^nonprofits/', include('nonprofits.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',views.index, name='index'),
    #url('.',views.export_to_csv, name='export'),
)
