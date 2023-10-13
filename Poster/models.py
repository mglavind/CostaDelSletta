from django.db import models
from django.urls import reverse

class Godkendelse(models.Model):

    # Relationships
    Opgave = models.ForeignKey("Poster.Opgave", on_delete=models.CASCADE)
    Hold = models.ForeignKey("Organization.Bruger", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Poster_Godkendelse_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Poster_Godkendelse_update", args=(self.pk,))
    





class Opgave(models.Model):

    # Fields
    name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Poster_Opgave_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Poster_Opgave_update", args=(self.pk,))