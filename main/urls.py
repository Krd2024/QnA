from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", index, name="index"),
    path("q/<id_question>/", q, name="q"),
    path("answer/<id_question>", answer, name="answer"),
    path("create/", gg, name="create"),
    path("user/<username>/", user, name="user"),
    path("user/info/<username>/", info, name="info"),
    path("user_profile/", user_profile, name="user_profile"),
    path("login/", CustomLoginView.as_view(), name="login"),
]
