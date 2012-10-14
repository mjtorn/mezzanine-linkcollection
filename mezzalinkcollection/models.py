# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.contrib.auth import models as auth_models

from mezzanine.core.models import SiteRelated, MetaData

from django.db import models

from . import managers

class Link(SiteRelated, MetaData):
    """A link that can be added
    """

    date_added = models.DateField()
    added_by = models.ForeignKey(auth_models.User)

    url = models.URLField(unique=True)
    title = models.CharField(max_length=255)

    featured = models.BooleanField(default=False, verbose_name='Featured?')

    objects = managers.LinkManager()

    def __unicode__(self):
        return self.url

    def get_absolute_url(self):
        return self.url

# EOF

