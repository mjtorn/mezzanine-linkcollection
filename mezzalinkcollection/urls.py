# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^links/', 'mezzalinkcollection.views.links')
)

# EOF

