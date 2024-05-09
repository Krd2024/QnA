from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.views import View

from main.models import Question, Answer, Rection
from django.contrib.auth.models import User
from .forms import QForm


def create(request, **kwargs):

    if request.method == "POST":
        form = QForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")

    form = QForm()
    context = {"form": form}
    return render(request, "main/create_qust_form.html", context)


def update(request, **kwargs):
    print(kwargs["question_id"])
    return render(request, "main/create_qust_form.html")


def delete(request, **kwargs): ...


def question(request, **kwargs):
    print(kwargs)
    try:
        question_obj = Question.objects.filter(id=kwargs["id_question"])
        context = {"question": question_obj}
        print(question_obj, "<<< ===== message object")
        return render(request, "questions.html", context)
    except Exception as e:
        print(e, "<<< eeeeee")
        return HttpResponse("err")


def login_in(request):
    return render(request, "login.html")


def user_profile(request):
    name = request.GET.get("username")
    objects_user = User.objects.get(username=name)

    user_question = Question.objects.filter(autor=objects_user)
    other_questions = Question.objects.exclude(autor_id=objects_user)
    context = {"user_question": user_question, "other_questions": other_questions}
    return render(request, "user_profile.html", context)
    return HttpResponse(f"Это тестовая страница : {name}")


class CustomLoginView(LoginView):
    # def get_success_url(self):
    #     return reverse_lazy("/")

    def post(self, request):
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
                "/user_profile?username=" + username
            )  # Замените 'home' на имя вашего URL-шаблона для главной страницы
        else:
            # Если аутентификация не удалась, показать ошибку входа
            return render(
                request,
                "login.html",
                {"error_message": "Неправильный логин или пароль"},
            )


def answer(request, id_question):
    print(request.GET)
    print(id_question)
    if request.method == "POST":
        print(request.POST.get("message"))
        # return HttpResponseClientRefresh()
        # awns = Answer.objects.create(autor=)
    print(request.POST)
    return render(request, "answer.html")
