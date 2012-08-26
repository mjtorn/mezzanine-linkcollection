# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.conf.urls.defaults import patterns, include, url

import rss

urlpatterns = patterns('',
    url(r'^links/rss$', rss.LinkFeed()),
    url(r'^links/$', 'mezzalinkcollection.views.links'),
)

# EOF

