from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.display_form, name="display_form"),
    path("submit/", views.make_openai_call_for_analysis, name="make_openai_call_for_analysis"),
]