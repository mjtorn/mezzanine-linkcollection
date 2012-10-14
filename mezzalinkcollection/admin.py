# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.contrib import admin

from . import models

import datetime

def mark_featured(modeladmin, request, queryset):
    queryset.update(featured=True)

def mark_not_featured(modeladmin, request, queryset):
    queryset.update(featured=False)


class LinkAdmin(admin.ModelAdmin):
    """Custom admin
    """

    fields = ('date_added', 'url', 'title', 'description', 'gen_description', 'added_by')
    list_display = ('title', 'date_added', 'featured', 'description', 'clickable_url')
    actions = (mark_featured, mark_not_featured)

    def clickable_url(self, bob):
        """So we can link out
        """

        return '<a href="%s">%s</a>' % (bob.url, bob.url)
    clickable_url.allow_tags = True

    def get_form(self, request, obj=None, **kwargs):
        """We do not want to autogenerate the description here
        """

        form = super(LinkAdmin, self).get_form(request, obj=obj, **kwargs)

        form.base_fields['date_added'].initial = datetime.datetime.now()
        form.base_fields['gen_description'].initial = False
        form.base_fields['added_by'].initial = request.user.id

        return form

admin.site.register(models.Link, LinkAdmin)

# EOF

