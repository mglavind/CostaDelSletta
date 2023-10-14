from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from . import models
from . import forms
from .forms import GodkendelseForm

from django.http import HttpResponse
from Organization.models import Bruger  # Import your Bruger model



class OpgaveListView(generic.ListView):
    model = models.Opgave
    form_class = forms.OpgaveForm


class OpgaveCreateView(generic.CreateView):
    model = models.Opgave
    form_class = forms.OpgaveForm


class OpgaveDetailView(generic.DetailView):
    model = models.Opgave
    form_class = forms.OpgaveForm


class OpgaveUpdateView(generic.UpdateView):
    model = models.Opgave
    form_class = forms.OpgaveForm
    pk_url_kwarg = "pk"


class OpgaveDeleteView(generic.DeleteView):
    model = models.Opgave
    success_url = reverse_lazy("Poster_Opgave_list")


class GodkendelseListView(generic.ListView):
    model = models.Godkendelse
    form_class = forms.GodkendelseForm


class GodkendelseCreateView(generic.CreateView):
    model = models.Godkendelse
    form_class = forms.GodkendelseForm


class GodkendelseDetailView(generic.DetailView):
    model = models.Godkendelse
    form_class = forms.GodkendelseForm


class GodkendelseUpdateView(generic.UpdateView):
    model = models.Godkendelse
    form_class = forms.GodkendelseForm
    pk_url_kwarg = "pk"


class GodkendelseDeleteView(generic.DeleteView):
    model = models.Godkendelse
    success_url = reverse_lazy("Poster_Godkendelse_list")


class HoldListView(generic.ListView):
    model = models.Hold
    form_class = forms.HoldForm


class HoldCreateView(generic.CreateView):
    model = models.Hold
    form_class = forms.HoldForm


class HoldDetailView(generic.DetailView):
    model = models.Hold
    form_class = forms.HoldForm


class HoldUpdateView(generic.UpdateView):
    model = models.Hold
    form_class = forms.HoldForm
    pk_url_kwarg = "pk"


class HoldDeleteView(generic.DeleteView):
    model = models.Hold
    success_url = reverse_lazy("Poster_Hold_list")



def by_post(request, opgave_id):
    try:
        opgave = models.Opgave.objects.get(pk=opgave_id)
        return HttpResponse(f"Displaying Opgave with ID {opgave_id}: {opgave.name}")  # Use the correct attribute, e.g., 'name'

    except models.Opgave.DoesNotExist:
        return HttpResponse("Opgave not found")

def by_bruger(request, bruger_id):
    try:
        hold = models.Hold.objects.get(pk=bruger_id)
        godkendelser = models.Godkendelse.objects.filter(Hold=hold)

        # Specify the template name
        template_name = 'Poster/godkendelse_by_bruger.html'

        # Render the template with the context data
        return render(request, template_name, {'godkendelser': godkendelser, 'hold': hold})

    except Bruger.DoesNotExist:
        return HttpResponse("Bruger not found")
    
