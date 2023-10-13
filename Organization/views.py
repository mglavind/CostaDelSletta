from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class BrugerListView(generic.ListView):
    model = models.Bruger
    form_class = forms.BrugerForm


class BrugerCreateView(generic.CreateView):
    model = models.Bruger
    form_class = forms.BrugerForm


class BrugerDetailView(generic.DetailView):
    model = models.Bruger
    form_class = forms.BrugerForm


class BrugerUpdateView(generic.UpdateView):
    model = models.Bruger
    form_class = forms.BrugerForm
    pk_url_kwarg = "pk"


class BrugerDeleteView(generic.DeleteView):
    model = models.Bruger
    success_url = reverse_lazy("organization_Bruger_list")