# -*- coding: utf-8 -*-
from django.db.models import Field
from django.conf import settings

from .widgets import UiKitWidget


class UiKitField(Field):
    def __init__(self, *args, **kwargs):
        mode = kwargs.pop('mode', 'split')
        markdown = kwargs.pop('markdown', False)
        self.widget = UiKitWidget(
            mode=mode,
            markdown=markdown,
        )
        super(UiKitField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "TextField"

    def formfield(self, **kwargs):
        defaults = {'widget': self.widget}
        defaults.update(kwargs)
        return super(UiKitField, self).formfield(**defaults)


if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules

    add_introspection_rules([], ["^uikit_editor\.fields\.UiKitField"])