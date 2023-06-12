from django.urls import path

from . import views

urlpatterns = [
    path("/new/", views.checklist_new, name="checklist-new"),
]