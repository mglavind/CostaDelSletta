from django import forms
from Poster.models import Opgave
from Organization.models import Bruger
from . import models


class OpgaveForm(forms.ModelForm):
    class Meta:
        model = models.Opgave
        fields = [
            "name",
            "description",
        ]


class GodkendelseForm(forms.ModelForm):
    class Meta:
        model = models.Godkendelse
        fields = [
            "status",
            "Opgave",
            "Hold",
        ]

    def __init__(self, *args, **kwargs):
        super(GodkendelseForm, self).__init__(*args, **kwargs)
        self.fields["Opgave"].queryset = Opgave.objects.all()
        self.fields["Hold"].queryset = Bruger.objects.all()

class HoldForm(forms.ModelForm):
    class Meta:
        model = models.Hold
        fields = [
            "role",
            "name",
            "description",
        ]