# django-cjswidget  [![PyPI](https://img.shields.io/pypi/v/django-cjswidget)](https://pypi.org/project/django-cjswidget/)
A replacement for the Select widget with fancy new features - powered by 
[choices.js](https://github.com/jshjohnson/Choices)!

## Install

1.  Add "cjswidget" to your `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'cjswidget',
]
```

## Use
Use in place of a normal select widget, that's all!
```python
from cjswidget.widgets import CJSWidget

class MyForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('country', 'region')
        widgets = {
            'country': CJSWidget(),
            'region': CJSWidget(options={'shouldSort': False}),
        }
```

## License

This software is released under the MIT license.
```
Copyright (c) 2019-2020 Luke Rogers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
