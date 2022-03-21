from dataclasses import fields
from django import forms
from . import models

class CorporatesForm(forms.ModelForm):
    class Meta:
        model=models.Corporates
        fields="__all__"

