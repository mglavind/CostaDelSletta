from django.contrib import admin
from django import forms

from . import models


class GodkendelseAdminForm(forms.ModelForm):

    class Meta:
        model = models.Godkendelse
        fields = "__all__"


class GodkendelseAdmin(admin.ModelAdmin):
    form = GodkendelseAdminForm
    list_display = [
        "Opgave",
        "Hold",
        "status",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class OpgaveAdminForm(forms.ModelForm):

    class Meta:
        model = models.Opgave
        fields = "__all__"


class OpgaveAdmin(admin.ModelAdmin):
    form = OpgaveAdminForm
    list_display = [
        "name",
        "description",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.Godkendelse, GodkendelseAdmin)
admin.site.register(models.Opgave, OpgaveAdmin)