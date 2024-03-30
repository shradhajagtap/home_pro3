from django.urls import path

from .views import employee_view, show_view, update_view, delete_view

urlpatterns = [
    path("", employee_view, name="employee_url"),
    path("show/", show_view, name="show_url"),
    path("update/<int:pk>", update_view, name="update_url"),
    path("delete/<int:pk>", delete_view, name="delete_url"),
]

