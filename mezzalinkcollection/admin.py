# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.contrib import admin

from . import models

class LinkAdmin(admin.ModelAdmin):
    """Custom admin
    """

    fields = ('date_added', 'url', 'title', 'description', 'gen_description', 'added_by')

    def get_form(self, request, obj=None, **kwargs):
        """We do not want to autogenerate the description here
        """

        form = super(LinkAdmin, self).get_form(request, obj=obj, **kwargs)

        ## FIXME: does not seem to work, maybe we got instantiated? investigate later
        form.base_fields['gen_description'].default = False
        form.base_fields['added_by'].default = request.user

        return form

admin.site.register(models.Link, LinkAdmin)

# EOF

