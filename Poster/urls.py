from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Godkendelse", api.GodkendelseViewSet)
router.register("Opgave", api.OpgaveViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Poster/Godkendelse/ministerie/<int:opgave_id>/", views.by_post),
    path("Poster/Godkendelse/hold/<int:bruger_id>/", views.by_bruger),
    path("Poster/Godkendelse/", views.GodkendelseListView.as_view(), name="Poster_Godkendelse_list"),
    path("Poster/Godkendelse/create/", views.GodkendelseCreateView.as_view(), name="Poster_Godkendelse_create"),
    path("Poster/Godkendelse/detail/<int:pk>/", views.GodkendelseDetailView.as_view(), name="Poster_Godkendelse_detail"),
    path("Poster/Godkendelse/update/<int:pk>/", views.GodkendelseUpdateView.as_view(), name="Poster_Godkendelse_update"),
    path("Poster/Godkendelse/delete/<int:pk>/", views.GodkendelseDeleteView.as_view(), name="Poster_Godkendelse_delete"),
    path("Poster/Opgave/", views.OpgaveListView.as_view(), name="Poster_Opgave_list"),
    path("Poster/Opgave/create/", views.OpgaveCreateView.as_view(), name="Poster_Opgave_create"),
    path("Poster/Opgave/detail/<int:pk>/", views.OpgaveDetailView.as_view(), name="Poster_Opgave_detail"),
    path("Poster/Opgave/update/<int:pk>/", views.OpgaveUpdateView.as_view(), name="Poster_Opgave_update"),
    path("Poster/Opgave/delete/<int:pk>/", views.OpgaveDeleteView.as_view(), name="Poster_Opgave_delete"),

)