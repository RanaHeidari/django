from django import forms

from django import forms
from . import models

class landingForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(landingForm, self).__init__(*args, **kwargs)
        for item in landingForm.visible_fields(self):
            item.field.widget.attrs['class'] = 'form-control'
        class Meta:
            model = models.message
            fields = '__all__'
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
