from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("symptom_analysys", views.symptom_analysis, name="sym_an"),
    path("problem/<str:problem_name>", views.problem, name="problem"),
    path("symptom/<str:symptom_name>", views.symptom, name="symptom"),
]