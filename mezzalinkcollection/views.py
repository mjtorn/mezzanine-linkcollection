# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.http import HttpResponse

from django.template import RequestContext
from django.template import loader

from . import models

def links(request, template_name='mezzalinkcollection/links.html'):
    """View for rendering links
    """

    context = {
        'links': models.Link.objects.all().order_by('-id').values()
    }
    req_ctx = RequestContext(request, context)

    tmpl = loader.get_template(template_name)
    s = tmpl.render(req_ctx)

    return HttpResponse(s, status=200, content_type='text/html')

# EOF

