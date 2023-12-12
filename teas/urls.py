from django.urls import path

from . import views

urlpatterns = [
    path("filter/", views.filter, name="filter"),
    path("<int:tea_id>/", views.details, name="details"),
]
