from django.urls import path
from .views import *
from . import auth_user_view
from main import views


urlpatterns = [
    #
    path("", index, name="index"),
    path("q/create/", create, name="question_create"),  # 1
    path("q/<int:question_id>/", question, name="question"),  # 1
    path("q/<int:question_id>/update/", update, name="question_update"),
    path("q/<int:question_id>/delete/", delete, name="question_delete"),  # 1
    #    #
    path("register/", auth_user_view.register, name="register"),
    path("login_in/", auth_user_view.login_in, name="login_in"),
    path("login/", auth_user_view.CustomLoginView.as_view(), name="login"),
    path("logout/", auth_user_view.logoutPage, name="logout"),
    #
    path("user/<str:username>/", user_profile, name="user_profile"),
    path(
        "user/<int:answer_id>/<str:choice>/",
        answer_update_delete,
        name="answer_update_delete",
    ),
    path(
        "user/<str:username>/<str:choice>/",
        info_user_choice,
        name="info_user_choice",
    ),
    path("user/<str:choice>/", info_user, name="info_user"),
    path("search/<str:search>/", search, name="search"),
    # path("answer/<str:choice>/", rection, name="rection"),
    path(
        "increase_counter/<int:answer_id>/",
        increase_counter,
        name="increase_counter",
    ),
    path("correct/<int:answer_id>/", correct, name="correct"),
]

# terminal.integrated.fontSize
