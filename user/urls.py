from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_user_info, name="get_user_info"),
    path("login/", views.login_user, name="login_user"),
]
