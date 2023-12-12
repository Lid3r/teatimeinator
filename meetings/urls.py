from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_all, name="get_all"),
    path("lets-meet/", views.add_to_meeting, name="add_to_meeting"),
    path("<int:meeting_id>/", views.details, name="details"),
]
