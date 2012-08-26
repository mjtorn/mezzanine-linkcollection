# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.contrib.syndication.views import Feed

from django.core.urlresolvers import reverse

from django.conf import settings

from django.shortcuts import get_object_or_404

from . import models

import datetime

import time

class LinkFeed(Feed):
    """Collected links
    """

    title = settings.LINKS_TITLE
    description = settings.LINKS_DESCRIPTION

    def get_object(self, request):
        """XXX: How is this even working?
        """
        return models.Link.objects.latest('id')

    def link(self, obj):
        return obj.get_absolute_url()

    def items(self):
        now = datetime.datetime.now()
        return models.Link.objects.all().select_related().order_by('-date_added')

    def item_author_name(self, obj):
        return '%s %s' % (obj.added_by.first_name, obj.added_by.last_name)

    def item_author_link(self, obj):
        """Do not fail if user reverses aren't set up
        """

        try:
            return reverse('user', args=(obj.added_by.username,))
        except Exception:
            return obj.get_absolute_url()

    def item_pubdate(self, obj):
        return datetime.datetime.fromtimestamp(time.mktime(obj.date_added.timetuple()))

    def item_title(self, obj):
        return obj.title

    def item_description(self, obj):
        return obj.description



# EOF

