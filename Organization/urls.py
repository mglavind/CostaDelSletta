from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register("Bruger", api.BrugerViewSet)

router = routers.DefaultRouter()

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Organization/Bruger/", views.BrugerListView.as_view(), name="Organization_Bruger_list"),
    path("Organization/Bruger/create/", views.BrugerCreateView.as_view(), name="Organization_Bruger_create"),
    path("Organization/Bruger/detail/<int:pk>/", views.BrugerDetailView.as_view(), name="Organization_Bruger_detail"),
    path("Organization/Bruger/update/<int:pk>/", views.BrugerUpdateView.as_view(), name="Organization_Bruger_update"),
    path("Organization/Bruger/delete/<int:pk>/", views.BrugerDeleteView.as_view(), name="Organization_Bruger_delete"),


)
