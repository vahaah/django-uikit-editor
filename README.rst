UiKit editor for Django
=======================

What's that
-----------

*uikit_editor* is a reusable application for Django, using `UiKit editor <http://getuikit.com/docs/addons_htmleditor.html>`_


Dependence
----------

- `Django >= 1.3`

Getting started
---------------

- Install *uikit_editor*:

```pip install uikit_editor```

- Add `'uikit_editor'` to INSTALLED_APPS.


Using in model
--------------

.. code-block:: python

    from django.db import models
    from uikit_editor import UiKitField

    class Entry(models.Model):
        title = models.CharField(max_length=250, verbose_name=u'Title')
        text = UiKitField(verbose_name=u'Text')

or use custom parametrs:

.. code-block:: python

    text = UiKitField(
        verbose_name=u'Text',
        mode="tab", # 'split', 'tab' default 'split'
        markdown=True #default False
    )

Using for only admin interface
------------------------------

.. code-block:: python

    from django import forms
    from uikit_editor import UiKitWidget
    from blog.models import Entry

    class EntryAdminForm(forms.ModelForm):
        class Meta:
            model = Entry
            widgets = {
               'text': UiKitWidget(),
            }

    class EntryAdmin(admin.ModelAdmin):
        form = EntryAdminForm

`UiKitWidget` takes the same parameters as `UiKitField`.



Contributing
------------

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request =]