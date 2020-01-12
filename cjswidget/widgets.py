from django.forms import widgets

import shortuuid


class CJSWidget(widgets.Select):
    template_name = 'cjswidget/widget.html'

    def __init__(self, options=None, **kwargs):
        super().__init__(**kwargs)
        self.uuid = shortuuid.uuid()

        if options is None:
            options = {}

        self.options = options
        self.options_id = 'options_' + self.uuid

    def get_context(self, *args):
        context = super().get_context(*args)
        context.update({
            'options': self.options,
            'options_id': self.options_id,
        })
        return context

    class Media:
        js = (
            'cjswidget/choices.min.js',
        )

        css = {
            'all': (
                'cjswidget/choices.min.css',
            )
        }
