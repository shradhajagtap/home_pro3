from django.urls import path

from .views import signup_view, login_view, logout_view, change_view

urlpatterns = [
    path("sighup/", signup_view, name="signup_url"),
    path("login/", login_view, name="login_url"),
    path("logout/", logout_view, name="logout_url"),
    path("change/", change_view, name="change_url")
]
