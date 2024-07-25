from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect

from ..forms import UserRegisterForm

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from ..forms import UserRegisterForm
from main.models import User


def signup(request):
    if request.method == "POST":

        form = UserRegisterForm(request.POST)
        # form = ProfileEditForm(request.POST)
        if form.is_valid():
            user = form.save()

            current_site = get_current_site(request)
            subject = "Activate Your Account"
            message = render_to_string(
                "email/account_activation_email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": default_token_generator.make_token(user),
                },
            )
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
            return redirect("account_activation_sent")
    else:
        form = UserRegisterForm()
    return render(request, "email/signup.html", {"form": form})


def account_activation_sent(request):
    return render(request, "email/account_activation_sent.html")


# views.py (добавьте эти функции)

from django.contrib.auth import login


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("index")
    else:
        return render(request, "email/account_activation_invalid.html")


def logoutPage(request):
    logout(request)
    return redirect("index")


def login_in(request):
    return render(request, "login.html")


# def register(request):
#     if request.method == "POST":

#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("login_in")
#     else:
#         form = UserRegisterForm()
#     return render(request, "main/register.html", {"form": form})


class CustomLoginView(LoginView):

    def post(self, request):
        print(request.GET, "<<<<<<< ========")
        # Обработка отправленной формы
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Проверка аутентификации пользователя
        user = authenticate(username=username, password=password)

        if user is not None:
            # Если пользователь существует и аутентификация прошла успешно, войти в систему
            login(request, user)
            return redirect(
                f"/user/{username}"
                # f"/user/"
            )
        else:
            # Если аутентификация не удалась, показать ошибку входа
            return render(
                request,
                "login.html",
                {"error_message": "Неправильный логин или пароль"},
            )
