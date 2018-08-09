"""
Definition of urls for DjangoWebProject1.
"""

from django.conf.urls import include, url
import HelloDjangoApp.views #HelloDjangoApp defined in apps.py, and views.py

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# ^ - start of line relative to site root
# $ - end of line relative to site root
# ie - ^$ (blank) converts to www.domain.com/ and ^dick$ shows www.domain.com/dick/
# not closing a url with $ matches it to ANY URL starting with that expression
# r - raw string - don't escape any characters in the string


urlpatterns = [

    url(r'^$', HelloDjangoApp.views.index, name='index'),
    url(r'^home$', HelloDjangoApp.views.index, name='home'),
    url(r'^about$',HelloDjangoApp.views.about,name='about'),
    url(r'^dangernoggin$',HelloDjangoApp.views.about,name='dangernoggin'),
    # Examples:
    # url(r'^$', DjangoWebProject1.views.home, name='home'),
    # url(r'^DjangoWebProject1/', include('DjangoWebProject1.DjangoWebProject1.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    
]
