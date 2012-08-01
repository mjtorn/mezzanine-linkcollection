# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.contrib.auth import models as auth_models

from mezzanine.core.models import SiteRelated, MetaData

from django.db import models

class Link(SiteRelated, MetaData):
    """A link that can be added
    """

    date_added = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(auth_models.User)

    url = models.URLField(unique=True)
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.url

# EOF

