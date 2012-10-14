from django.db import models

class LinkManager(models.Manager):
    """To add some methods
    """

    def get_featured(self, **kwargs):
        """Featured links, use with your template
        """

        return self.filter(featured=True, **kwargs)

# EOF

