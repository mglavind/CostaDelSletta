from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser



class Bruger(AbstractUser):

    # Fields
    username = models.CharField(max_length=30, unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    role = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Organization_Bruger_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Organization_Bruger_update", args=(self.pk,))