from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("user/<username>/", user, name="user"),
    path("q/<id_question>/", q, name="q"),
]
