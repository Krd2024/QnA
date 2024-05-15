from django.urls import path
from .views import *
from . import auth_user_view


urlpatterns = [
    path("", index, name="index"),
    path("q/<int:question_id>/", question, name="question"),  # 1
    path("q/<int:question_id>/delete/", delete, name="question_delete"),  # 1
    path("q/create/", create, name="question_create"),  # 1
    path("q/<int:question_id>/update/", update, name="question_update"),
    #    #
    path("register/", auth_user_view.register, name="register"),
    path("login_in/", auth_user_view.login_in, name="login_in"),
    path("login/", auth_user_view.CustomLoginView.as_view(), name="login"),
    path("logout/", auth_user_view.logoutPage, name="logout"),
    #
    path("user/<str:username>/", user_profile, name="user_profile"),
    path(
        "user/<str:username>/<str:choice>/",
        info_user_choice,
        name="info_user_choice",
    ),
    #
    # path(
    #     "q/update/<int:question_id>/", update, name="question_update"
    # ),  # местами поменять
    # path("user_profile/register", register, name="register"),  # 0
    path(
        "user_profile/get_answer/<int:question_id>", get_answer, name="get_answer"
    ),  # 0
    path("get_answer/<int:question_id>", get_answer, name="get_answer"),
    #
    #
    #
    path("user/<str:choice>/", info_user, name="info_user"),
    #
]
