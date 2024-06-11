from django.urls import path
from . import views
from . import auth_user_view
from main import views, auth_user_view

from . import rrr

urlpatterns = [
    #
    # path(
    #     "test/",
    #     rrr.test2,
    # ),  # 1
    path("", views.index, name="index"),
    path("q/create/", views.create, name="question_create"),  # 1
    path("q/<int:question_id>/", views.question, name="question"),  # 1
    path("q/<int:question_id>/update/", views.update, name="question_update"),
    path("q/<int:question_id>/delete/", views.delete, name="question_delete"),  # 1
    #    #
    path("register/", auth_user_view.register, name="register"),
    path("login_in/", auth_user_view.login_in, name="login_in"),
    path("login/", auth_user_view.CustomLoginView.as_view(), name="login"),
    path("logout/", auth_user_view.logoutPage, name="logout"),
    #
    #
    path("user/<str:username>/", views.user_profile, name="user_profile"),
    path("user/<str:username>/edit_profile/", views.edit_profile, name="edit_profile"),
    path(
        "user/<int:answer_id>/<str:choice>/",
        views.answer_update_delete,
        name="answer_update_delete",
    ),
    # path(
    #     "user/<str:username>/<str:choice>/",
    #     info_user_choice,
    #     name="info_user_choice",
    # ),
    path("search/<str:search>/", views.search, name="search"),
    #
    path(
        "increase_counter/<int:answer_id>/",
        views.increase_counter,
        name="increase_counter",
    ),
    #
    path("correct/<int:answer_id>/", views.correct, name="correct"),
    #
    path("users/", views.all_users, name="all_users"),
    path("users/page/<str:page>", views.all_users, name="users_page"),
    #
    path("help/rating/", views.rating, name="rating"),
    #
    path("upload/", views.image_upload_view, name="upload"),
    #
    #
    path("signup/", auth_user_view.signup, name="signup"),
    path(
        "account_activation_sent/",
        auth_user_view.account_activation_sent,
        name="account_activation_sent",
    ),
    path("activate/<uidb64>/<token>/", auth_user_view.activate, name="activate"),
    #
    path("pars_up/<str:value>", views.pars_up, name="pars_up"),  # 1
]

# terminal.integrated.fontSize
