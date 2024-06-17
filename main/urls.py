from django.urls import path

from main.auth import auth_user_view
from . import views_1
from .auth import auth_user_view
from main import views_1
from main.views import questions, user
from . import rrr
from main.image import image

# from main.user_profile import user_profile_up
# from main.user_profile_update import user_profile_up

urlpatterns = [
    #
    # path(
    #     "test/",
    #     rrr.test2,
    # ),
    path("", views_1.index, name="index"),
    path("q/create/", questions.create, name="question_create"),  # 1
    path("q/<int:question_id>/", questions.question, name="question"),  # 1
    path("q/<int:question_id>/update/", questions.update, name="question_update"),
    path("q/<int:question_id>/delete/", questions.delete, name="question_delete"),  # 1
    #    #
    path("register/", auth_user_view.register, name="register"),
    path("login_in/", auth_user_view.login_in, name="login_in"),
    path("login/", auth_user_view.CustomLoginView.as_view(), name="login"),
    path("logout/", auth_user_view.logoutPage, name="logout"),
    #
    path("user/<str:username>/", user.user_profile, name="user_profile"),
    #
    path(
        "user/<str:username>/edit_profile/",
        user.edit_profile,
        name="edit_profile",
    ),
    #
    path(
        "user/<int:answer_id>/<str:choice>/",
        user.answer_update_delete,
        name="answer_update_delete",
    ),
    # path(
    #     "user/<str:username>/<str:choice>/",
    #     info_user_choice,
    #     name="info_user_choice",
    # ),
    path("search/<str:search>/", views_1.search, name="search"),
    #
    path(
        "increase_counter/<int:answer_id>/",
        views_1.increase_counter,
        name="increase_counter",
    ),
    #
    path("correct/<int:answer_id>/", views_1.correct, name="correct"),
    #
    path("users/", views_1.all_users, name="all_users"),
    path("users/page/<str:page>", views_1.all_users, name="users_page"),
    #
    path("help/rating/", views_1.rating, name="rating"),
    #
    path("upload/", image.image_upload_view, name="upload"),
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
    path("pars_up/<str:value>", views_1.pars_up, name="pars_up"),  # 1
    path("tegs", views_1.tegs, name="tegs"),
    path("tegs/<str:tegs>", views_1.questions_in_tag, name="questions_in_tag"),
    path("tegs/add/", views_1.add_tag, name="add_tag"),
]

# terminal.integrated.fontSize
