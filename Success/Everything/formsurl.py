from django.contrib import admin
from django.urls import path
from Everything import views
from django.urls import include, path


app_name = "Everything"


urlpatterns = [
    path("Relative/",views.Relative, name = "relative"),
    path("Other/", views.Other, name = "Other"),
    


]

#Template Tagging
