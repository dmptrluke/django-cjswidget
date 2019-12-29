from django.forms import widgets


class CJSWidget(widgets.Select):
    template_name = 'cjswidget/widget.html'

    class Media:
        js = (
            'cjswidget/choices.min.js',
        )

        css = {
            'all': (
                'cjswidget/choices.min.css',
            )
        }
