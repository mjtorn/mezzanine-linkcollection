# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.conf.urls import include, url
from mezzalinkcollection.views import links as links_view

from . import rss

urlpatterns = [
    url(r'^links/rss$', rss.LinkFeed()),
    url(r'^links/$', links_view),
]

# EOF

