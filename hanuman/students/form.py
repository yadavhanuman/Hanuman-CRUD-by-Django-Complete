from django import forms
from .models import *


class studentForm(forms.ModelForm):
    class Meta:
        model= register

        fields='__all__'
      




