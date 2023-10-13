from django import forms
from . import models


class BrugerForm(forms.ModelForm):
    class Meta:
        model = models.Bruger
        fields = [
            "username",
            "role",
        ]