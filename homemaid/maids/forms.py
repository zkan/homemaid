from django import forms
from django.forms import ModelForm

from .models import Maid


# class MaidForm(Form):
#     name = forms.TextInput()
#     ...


class MaidForm(ModelForm):
    class Meta:
        model = Maid
        fields = ('name', )