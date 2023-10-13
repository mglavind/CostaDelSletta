import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Opgave_list_view(client):
    instance1 = test_helpers.create_Poster_Opgave()
    instance2 = test_helpers.create_Poster_Opgave()
    url = reverse("Poster_Opgave_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Opgave_create_view(client):
    url = reverse("Poster_Opgave_create")
    data = {
        "description": "text",
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Opgave_detail_view(client):
    instance = test_helpers.create_Poster_Opgave()
    url = reverse("Poster_Opgave_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Opgave_update_view(client):
    instance = test_helpers.create_Poster_Opgave()
    url = reverse("Poster_Opgave_update", args=[instance.pk, ])
    data = {
        "description": "text",
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Godkendelse_list_view(client):
    instance1 = test_helpers.create_Poster_Godkendelse()
    instance2 = test_helpers.create_Poster_Godkendelse()
    url = reverse("Poster_Godkendelse_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Godkendelse_create_view(client):
    Hold = test_helpers.create_Organization_Bruger()
    Opgave = test_helpers.create_Poster_Opgave()
    url = reverse("Poster_Godkendelse_create")
    data = {
        "Status": "text",
        "Hold": Hold.pk,
        "Opgave": Opgave.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Godkendelse_detail_view(client):
    instance = test_helpers.create_Poster_Godkendelse()
    url = reverse("Poster_Godkendelse_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Godkendelse_update_view(client):
    Hold = test_helpers.create_Organization_Bruger()
    Opgave = test_helpers.create_Poster_Opgave()
    instance = test_helpers.create_Poster_Godkendelse()
    url = reverse("Poster_Godkendelse_update", args=[instance.pk, ])
    data = {
        "Status": "text",
        "Hold": Hold.pk,
        "Opgave": Opgave.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
