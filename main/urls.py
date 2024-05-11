from django.urls import path
from .views import *
from .views_2 import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", index, name="index"),
    #
    # path("test/", test2, name="test2"),
    #
    path("q/<int:id_question>/", question, name="question"),
    path("q/<int:id_question>/<str:username>/", question, name="question"),
    #
    # path("q/delete/<int:question_id>/", delete, name="question_delete"),
    path("q/delete/<int:question_id>/<str:name>", delete, name="question_delete"),
    #
    path("q/update/<int:question_id>/", update, name="question_update"),
    path("q/create/", create, name="question_create"),
    #
    path("register/", register, name="register"),
    path("user_profile/", user_profile, name="user_profile"),
    path("user_profile/register/", register, name="register"),
    path("user_profile/get_answer/<int:id_question>", get_answer, name="get_answer"),
    path("get_answer/<int:id_question>", get_answer, name="get_answer"),
    #
    path("user_profile/login_in/", login_in, name="login_in"),
    path("login_in/", login_in, name="login_in"),
    path("login/", CustomLoginView.as_view(), name="login"),
    #
    path("answer/<int:id_question>/<str:username>/", answer, name="answer"),
    #
    path("user/info/<username>/", info, name="info"),
    path("user/<username>/", user, name="user"),
]
