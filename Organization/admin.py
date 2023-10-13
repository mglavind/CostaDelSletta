from django.contrib import admin
from django import forms

from . import models


class BrugerAdminForm(forms.ModelForm):

    class Meta:
        model = models.Bruger
        fields = "__all__"


class BrugerAdmin(admin.ModelAdmin):
    form = BrugerAdminForm
    list_display = [
        "username",
        "role",

    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.Bruger, BrugerAdmin)