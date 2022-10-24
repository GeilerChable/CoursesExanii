from django.urls import path 
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("1/", views.math, name="math"),
    path("2/", views.english, name="english"),
    path("3/", views.espanol, name="spanish"),
    path("inscription/", views.inscription, name="inscription")
]