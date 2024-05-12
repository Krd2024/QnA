from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.views import View

from main.models import Question, Answer, Rection
from django.contrib.auth.models import User

# from django_htmx.http import HttpResponseClientRefresh


# def answer(request, id_question):
#     print(request.GET)
#     print(id_question)
#     if request.method == "POST":
#         print(request.POST.get("message"))
#         # return HttpResponseClientRefresh()
#     print(request.POST)
#     return render(request, "answer.html")


# from django.contrib.auth.models import User
# def user_profile(request):
#     name = request.GET.get("username")
#     objects_user = User.objects.get(username=name)

#     user_question = Question.objects.filter(autor=objects_user)
#     context = {"user_question": user_question}
#     return render(request, "user_profile.html", context)
#     return HttpResponse(f"Это тестовая страница : {name}")


# class CustomLoginView(LoginView):
#     # def get_success_url(self):
#     #     return reverse_lazy("/")

#     def post(self, request):
#         # Обработка отправленной формы
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         print(username, password)

#         # Проверка аутентификации пользователя
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             # Если пользователь существует и аутентификация прошла успешно, войти в систему
#             login(request, user)
#             return redirect(
#                 "/user_profile?username=" + username
#             )  # Замените 'home' на имя вашего URL-шаблона для главной страницы
#         else:
#             # Если аутентификация не удалась, показать ошибку входа
#             return render(
#                 request,
#                 "login.html",
#                 {"error_message": "Неправильный логин или пароль"},
#             )


# def index(request):
#     user = User.objects.get(username="Den")

#     all_question = Question.objects.all()

#     context = {"all_question": all_question}

#     return render(request, "main/index_main.html", context)


def user(request):
    return render(request, "index.html")


def gg(request):
    print("yes")
    # user = User.objects.get(username="Sem")
    # lst_q = [
    #     "Какие основные методы для работы со строками существуют в Python?",
    #     "Что такое исключения (exceptions) в Python, и как их обрабатывать?",
    #     "Как создать функцию (def) в Python, и как передать ей аргументы?",
    #     "Чем отличаются методы `append()` и `extend()` для списка в Python?",
    #     "Каким образом можно выполнить чтение и запись данных в файле в Python?",
    # ]
    # for item in lst_q:
    #     zapis = Question.objects.create(autor=user, title="Python", text=item)
    #     zapis.save()
    # ==============================================
    # x = User.objects.create(username="new_user", password="12345")
    # x.save()
    # print(x)
    return render(request, "index.html")
