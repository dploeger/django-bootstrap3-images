""" Bootstrap3 image field """

from django.db import models
from widgets import Bootstrap3ImageSelector


class Bootstrap3ImageField(models.CharField):

    max_length=200

    """ The bootstrap3 image field
    """

    def formfield(self, **kwargs):

        kwargs['widget'] = Bootstrap3ImageSelector

        return super(Bootstrap3ImageField, self).formfield(**kwargs)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules(
        [],
        ["^bootstrap3_images\.fields\.Bootstrap3ImageField"]
    )
except ImportError:
    pass

