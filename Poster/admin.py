from django.contrib import admin
from django import forms
from typing import List
from django import forms
from django.urls.resolvers import URLPattern
from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from . import models
import csv


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
    list_filter = (
        ('Opgave', RelatedDropdownFilter),
        ('Hold', RelatedDropdownFilter),
    )
    search_fields = ['Opgave__name', 'Hold__name'] 


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

class HoldAdminForm(forms.ModelForm):

    class Meta:
        model = models.Hold
        fields = "__all__"

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class HoldAdmin(admin.ModelAdmin):
    form = HoldAdminForm
    list_display = [
        'id',
        "name",
        "gruppe_name",
        "role",
        "description",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]
    def get_urls(self) -> List[URLPattern]:
            urls = super().get_urls()
            new_urls = [path('upload-csv/', self.upload_csv),]
            return new_urls + urls
    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith(".csv"):
                messages.warning(request, "Wrong file type was uploaded. Please upload a CSV file.")
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for line in csv_data:
                fields = line.split(";")
                name = fields[0]
                gruppe_name = fields[1]
                role = fields[2]
                description = fields[3]
                

                # Check if the name is unique
                if models.Hold.objects.filter(name=name).exists():
                    messages.warning(request, f"Item with name '{name}' already exists.")
                    continue

                form_data = {
                    "name": name,
                    "gruppe_name": gruppe_name,
                    "role": role,
                    "description": description,
                }

                # Create a LocationItemAdminForm instance with the modified form_data
                form = HoldAdminForm(form_data)

                if form.is_valid():
                    # Save the LocationItem instance
                    location_item = form.save()

                else:
                    error_messages = []
                    for field, errors in form.errors.items():
                        error_messages.append(f"Field '{field}': {'; '.join(map(str, errors))}")
                    error_message = "; ".join(error_messages)
                    messages.warning(request, f"Invalid data in CSV: {error_message}")

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)



admin.site.register(models.Godkendelse, GodkendelseAdmin)
admin.site.register(models.Opgave, OpgaveAdmin)
admin.site.register(models.Hold, HoldAdmin)