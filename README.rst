====
mezzanine-linkcollection
====

Collect links. Feature them. Share them over RSS.

Installation
============

Add this to settings.py::

    INSTALLED_APPLICATIONS = (
        ...
        'mezzalinkcollection',
        ...
    )


And this to urls.py, just above the Mezzanine urls::

    (r'^', include('mezzalinkcollection.urls')),


If you want to have the featured links in every request, there's a context processor::

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'mezzalinkcollection.context_processors.links',
        ...
    )


Customization
=============

The templates are currently horrible. Please send a pull request my way so I
can update them ;)

If you use the context processors, you can access ``featured_links`` in your
template.


