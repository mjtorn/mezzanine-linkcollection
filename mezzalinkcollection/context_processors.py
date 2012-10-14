from . import models

def links(request):
    return {
        'featured_links': models.Link.objects.get_featured().order_by('date_added')
    }

# EOF

