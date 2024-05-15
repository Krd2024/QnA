from django.urls import path
from .views import *
from .views_2 import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", index, name="index"),
    path("q/<int:id_question>/", question, name="question"),  # 1
    path("q/<int:question_id>/delete/", delete, name="question_delete"),  # 1
    path("q/create/", create, name="question_create"),  # 1
    path("q/<int:question_id>/update/", update, name="question_update"),
    path("q/delete/<int:question_id>/<str:name>", delete, name="question_delete"),  # 0
    #
    path("<int:id_question>/answer/", answer, name="answer"),
    #
    path("register/", register, name="register"),
    path("login_in/", login_in, name="login_in"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", logoutPage, name="logout"),
    #
    path("user/<str:username>/", user_profile, name="user_profile"),
    #
    # path(
    #     "q/update/<int:question_id>/", update, name="question_update"
    # ),  # местами поменять
    # path("user_profile/register", register, name="register"),  # 0
    path(
        "user_profile/get_answer/<int:id_question>", get_answer, name="get_answer"
    ),  # 0
    path("get_answer/<int:id_question>", get_answer, name="get_answer"),
    #
    #
    #
    path("user/<str:choice>/", info_user, name="info_user"),
    path(
        "user/info/get/<str:choice>/<str:name>/",
        info_user_choice,
        name="info_user_choice",
    ),
    #
    path("user/<username>/", user, name="user"),
    path("test", gg, name="user"),
]
