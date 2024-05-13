from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.views import View

from main.models import Question, Answer, Rection
from django.contrib.auth.models import User
from .forms import QForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# from rest_framework.views import APIView

from .forms import UserRegisterForm


def info_user_choice(request, **kwargs):
    try:
        print(kwargs)
        if kwargs.get("choice") == "questions":
            username = kwargs.get("name")
            user_obj = User.objects.get(username=username)
            user_quest_obj = Question.objects.filter(autor=user_obj)
            context = {"user_quest": user_quest_obj, "username": user_obj}
            return render(request, "user_info.html", context)

        if kwargs.get("choice") == "answer":
            username = kwargs.get("name")
            user_obj = User.objects.get(username=username)
            user_answer_obj = Answer.objects.filter(autor=user_obj)
            context = {"user_answer": user_answer_obj, "username": user_obj}
            return render(request, "user_info.html", context)
    except Exception as e:
        print(e)
        return render(request, "user_info.html")

    return HttpResponse("1234")
    # try:
    #     if kwargs.get("choice") == "questions":


def info_user(request, **kwargs):
    print(kwargs)
    try:
        username = kwargs.get("choice")
        user_obj = User.objects.filter(username=username)
        context = {"username": user_obj[0]}
        return render(request, "user_info.html", context)
    except Exception as e:
        print(e)
        return HttpResponse("1234")


def index(request):
    answers = (
        # Answer.objects.filter(question__in=other_questions)
        Answer.objects.all()
        .values("question_id")
        .annotate(total=Count("question_id"))
    )
    user = User.objects.get(username="Den")

    all_question = Question.objects.all()

    context = {
        "all_question": all_question,
        "answers": answers,
    }

    return render(request, "main/index_main.html", context)


def get_answer(request, **kwargs):

    print(kwargs["id_question"], "<<<< ----kwargs")
    question_obj = Question.objects.filter(id=kwargs["id_question"])[0]
    print(question_obj)
    answer_obj = Answer.objects.filter(question=question_obj)

    for answer in answer_obj:
        print(answer)
    context = {"answers": answer_obj}
    return render(request, "answer.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_in")
    else:
        form = UserRegisterForm()
    return render(request, "main/register.html", {"form": form})


@login_required(login_url="/login")
def create(request, **kwargs):

    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect("index")

    # form = QForm()
    form = QForm(initial={"autor": request.user})

    context = {"form": form}
    return render(request, "main/create_qust_form.html", context)


def update(request, **kwargs):
    print(kwargs["question_id"])
    if request.method == "POST":
        form = QForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")

    question_obj = Question.objects.filter(id=kwargs["question_id"])
    print(question_obj[0].text, "<<< -----  question_obj[0].text  ")
    form = QForm(initial={"text": question_obj[0].text, "autor": question_obj[0].autor})
    context = {"form": form}
    return render(request, "main/update_qust_form.html", context)


def delete(request, **kwargs):
    print(kwargs.get("name"), "---1")
    print(kwargs["name"], "---2")

    try:
        print(kwargs["question_id"])
        Question.objects.filter(id=kwargs["question_id"]).delete()
        # user_profile(request)
        name = kwargs.get("name")
        print(name)
        objects_user = User.objects.get(username=name)
        user_question = Question.objects.filter(autor=objects_user)
        other_questions = Question.objects.exclude(autor_id=objects_user)
        context = {
            "user_question": user_question,
            "other_questions": other_questions,
            "username": objects_user,
        }
    except Exception as e:
        print(e)
    return render(request, "user_profile.html", context)


def question(request, **kwargs):

    print(kwargs, "<<<< ---------- kwargs ----------")
    try:
        objects_user = kwargs.get("username")
        question_obj = Question.objects.get(id=kwargs["id_question"])
        context = {"questG": question_obj, "username": objects_user}
        print(question_obj, "<<< ===== message object")
        print(question_obj.answers)
        return render(request, "questions.html", context)
    except Exception as e:
        print(e, "<<< eeeeee")
        return HttpResponse("err")


def login_in(request):
    return render(request, "login.html")


def user_profile(request):
    name = request.GET.get("username")
    objects_user = User.objects.get(username=name)
    print(objects_user, "  <<<         obj_user")

    user_question = Question.objects.filter(autor=objects_user)
    other_questions = Question.objects.exclude(autor_id=objects_user)
    # answers = Answer.objects.filter(question__in=other_questions)
    # answers = Answer.objects.all()
    answers = (
        # Answer.objects.filter(question__in=other_questions)
        Answer.objects.all()
        .values("question_id")
        .annotate(total=Count("question_id"))
    )

    context = {
        "user_question": user_question,
        "other_questions": other_questions,
        "username": objects_user,
        "answers": answers,
    }

    # =================================================================
    #
    return render(request, "user_profile.html", context)


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


def answer(request, id_question, username):
    """Ответ на вопрос"""
    # print(request.GET)
    try:
        print(id_question, "<<< id вопроса")
        print(username, "<<< Кто ответил")
        if request.method == "POST":
            print(request.POST.get("message"), "<<< текст ответа")
            # return HttpResponseClientRefresh()
            autor_obj = User.objects.get(username=username)
            question_obj = Question.objects.get(id=id_question)
            text = request.POST.get("message")
            awnswer_add = Answer.objects.create(
                autor=autor_obj, question=question_obj, text=text
            )
            awnswer_add.save()

        print(request.POST)
        return redirect("/user_profile/?username=" + username)
        # return render(request, "answer.html")
    except Exception as e:
        print(e)
        return render(request, "login.html")
        return HttpResponse("Наверно нужно сначала войти ")


def logoutPage(request):
    logout(request)
    return redirect("index")
