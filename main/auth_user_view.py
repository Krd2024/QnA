from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect

from .forms import UserRegisterForm


def logoutPage(request):
    logout(request)
    return redirect("index")


def login_in(request):
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_in")
    else:
        form = UserRegisterForm()
    return render(request, "main/register.html", {"form": form})


class CustomLoginView(LoginView):

    def post(self, request):
        print(request.GET, "<<<<<<< ========")
        # Обработка отправленной формы
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)

        # Проверка аутентификации пользователя
        user = authenticate(username=username, password=password)

        if user is not None:
            # Если пользователь существует и аутентификация прошла успешно, войти в систему
            login(request, user)
            return redirect(
                f"/user/{username}"
                # f"/user/"
            )  # Замените 'home' на имя вашего URL-шаблона для главной страницы
        else:
            # Если аутентификация не удалась, показать ошибку входа
            return render(
                request,
                "login.html",
                {"error_message": "Неправильный логин или пароль"},
            )
