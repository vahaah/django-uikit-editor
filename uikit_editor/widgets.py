# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django import forms


try:
    from django.forms.utils import flatatt
except ImportError:
    from django.forms.util import flatatt
from django.utils.safestring import mark_safe


class UiKitWidget(forms.Textarea):
    def __init__(self, mode='split', markdown=False, *args, **kwargs):
        self.mode = mode
        self.markdown = markdown
        super(UiKitWidget, self).__init__(*args, **kwargs)

    @property
    def media(self):
        js = [
            "uikit_editor/jquery.js",
            "uikit_editor/uikit/js/uikit.min.js",
            "uikit_editor/codemirror/lib/codemirror.js",
            "uikit_editor/codemirror/mode/markdown/markdown.js",
            "uikit_editor/codemirror/addon/mode/overlay.js",
            "uikit_editor/codemirror/mode/xml/xml.js",
            "uikit_editor/codemirror/mode/gfm/gfm.js",
            "uikit_editor/marked/marked.js",
            "uikit_editor/uikit/js/components/htmleditor.js"
        ]
        css = {
            "screen": [
                "uikit_editor/uikit/css/uikit.min.css",
                "uikit_editor/codemirror/lib/codemirror.css",
                "uikit_editor/uikit/css/components/htmleditor.css",
            ],
        }
        return forms.Media(js=js, css=css)

    def render(self, name, value, attrs=None):
        attrs = attrs or {}
        attrs['data-uk-htmleditor'] = json.dumps({'mode': self.mode, 'markdown': self.markdown})
        textarea = super(UiKitWidget, self).render(name, value, attrs)
        return mark_safe(textarea)