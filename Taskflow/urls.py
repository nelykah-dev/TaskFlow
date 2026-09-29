from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    
    path("",views.liste_taches , name="liste_taches"),
    path("creer_tache", views.creer_tache, name="creer_tache"),
]
