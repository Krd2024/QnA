from django.urls import path
from .views import *
from .views_2 import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", index, name="index"),
    #
    #
    #
    path("q/<int:id_question>/", question, name="question"),
    # path("q/<int:id_question>/delete", delete, name="question_delete"),
    path("q/<int:question_id>/delete/", delete, name="question_delete"),
    path("q/<int:question_id>/update", update, name="question_update"),
    path("q/create/", create, name="question_create"),
    #
    #
    #
    # path("answer/<id_question>", answer, name="answer"),
    # path("create/", gg, name="create"),
    # path("user/<username>/", user, name="user"),
    # path("user/info/<username>/", info, name="info"),
    # path("user_profile/", user_profile, name="user_profile"),
    # path("login/", CustomLoginView.as_view(), name="login"),
]
