# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.shortcuts import render_to_response

from django.template import RequestContext

from . import models

def links(request, template_name='mezzalinkcollection/links.html'):
    """View for rendering links
    """

    context = {
        'links': models.Link.objects.all().order_by('-id').values()
    }
    req_ctx = RequestContext(request, context)

    return render_to_response(template_name, req_ctx)

# EOF

