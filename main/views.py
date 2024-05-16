from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.models import Question, Answer
from django.contrib.auth.models import User
from .forms import QForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required


def info_user_choice(request, **kwargs):
    # username = request.user
    try:
        print(kwargs)
        if kwargs.get("choice") == "questions":
            username = kwargs.get("username")
            user_obj = User.objects.get(username=username)
            user_quest_obj = Question.objects.filter(autor=user_obj)
            context = {
                "user_quest": user_quest_obj,
                "user_question": len(user_quest_obj),
                "username": username,
            }

            return render(request, "profile.html", context)
            # return render(request, "user_info.html", context)

        if kwargs.get("choice") == "answer":
            username = kwargs.get("name")
            user_obj = User.objects.get(username=username)
            user_answer_obj = Answer.objects.filter(autor=user_obj)

            # context = {"user_answer": user_answer_obj}
            context = {"user_answer": user_answer_obj, "answers": len(user_answer_obj)}
            return render(request, "profile.html", context)
            # return render(request, "user_info.html", context)
    except Exception as e:
        print(e)
        return render(request, "profile.html")

    return HttpResponse("1234")
    # try:
    #     if kwargs.get("choice") == "questions":


def info_user(request, **kwargs):
    # username = request.user
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

    print(kwargs["question_id"], "<<<< ----kwargs")
    question_obj = Question.objects.filter(id=kwargs["question_id"])[0]
    print(question_obj)
    answer_obj = Answer.objects.filter(question=question_obj)

    for answer in answer_obj:
        print(answer)
    context = {"answers": answer_obj}
    return render(request, "answer.html", context)


# def register(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("login_in")
#     else:
#         form = UserRegisterForm()
#     return render(request, "main/register.html", {"form": form})


# @login_required(login_url="/login_in")
# def create(request, **kwargs):

#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#         return redirect("index")
#     # form = QForm()
#     form = QForm(initial={"autor": request.user})
#     context = {"form": form}
#     return render(request, "main/create_qust_form.html", context)


def update(request, **kwargs):
    # print(kwargs["question_id"])
    if request.method == "POST":
        form = QForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # for key, value in request.POST.items():
            #     print(f"Field: {key}, Value: {value}")
            question_id = kwargs["question_id"]
            question = Question.objects.get(id=question_id)
            question.title = form.cleaned_data["title"]
            question.text = form.cleaned_data["text"]
            question.teg = form.cleaned_data["teg"]
            question.save()

        return redirect(f"/user/{request.user}/")
    else:
        question_obj = Question.objects.filter(id=kwargs["question_id"])
        # print(question_obj[0].text, "<<< -----  question_obj[0].text  ")
        form = QForm(
            initial={"text": question_obj[0].text, "autor": question_obj[0].autor}
        )
        context = {"form": form}
        return render(request, "main/update_qust_form.html", context)


def delete(request, **kwargs):
    # print(kwargs.get("name"), "---1")
    # print(kwargs["name"], "---2")

    try:

        Question.objects.filter(id=kwargs["question_id"]).delete()
        # user_profile(request)
        user = request.user
        # objects_user = User.objects.get(username=name)
        # user_question = Question.objects.filter(autor=objects_user)
        user_question = Question.objects.filter(autor=user)
        # other_questions = Question.objects.exclude(autor_id=objects_user)
        other_questions = Question.objects.exclude(autor_id=user)
        context = {
            "user_question": user_question,
            "other_questions": other_questions,
            "username": user,
            # "username": objects_user,
        }
    except Exception as e:
        print(e)
    return render(request, "user_profile.html", context)


def question(request, **kwargs):
    """Выводит один вопрос и ответы к нему"""

    print(kwargs, "<<<< ---------- kwargs ----------")
    try:
        question_obj = Question.objects.get(id=kwargs["question_id"])
        if request.method == "POST":
            if not request.user.is_authenticated:
                return redirect("login")

            autor_obj = User.objects.get(username=request.user)
            question_obj = Question.objects.get(id=kwargs["question_id"])
            text = request.POST.get("message")
            awnswer_add = Answer.objects.create(
                autor=autor_obj, question=question_obj, text=text
            )
            awnswer_add.save()

            return redirect("question", kwargs["question_id"])
        # return redirect(f"/q/{kwargs["question_id"]}")

        context = {"quest": question_obj}
        print(question_obj, "<<< ===== message object")

        return render(request, "questions.html", context)
    except Exception as e:
        print(e, "<<< eeeeee")
        return HttpResponse("err")


# def login_in(request):
#     return render(request, "login.html")


def user_profile(request, *args, **kwargs):
    user = kwargs["username"]
    print(request.GET.get("q"))
    if request.GET.get("q") == "questions":
        print(12345)
        objects_user = User.objects.get(username=user)
        user_question = Question.objects.filter(autor=objects_user)
        context = {
            "user_question": user_question,
        }

        return render(request, "test.html", context)

    if request.GET.get("q") == "answers":
        print(12345)
        return render(request, "test2.html")

    objects_user = User.objects.get(username=user)
    user_question = Question.objects.filter(autor=objects_user)

    answers_1 = (
        Answer.objects.all().values("question_id").annotate(total=Count("question_id"))
    )

    answers = Answer.objects.filter(autor=objects_user)
    context = {
        "user_question": len(user_question),
        "username": objects_user,
        "answers": len(answers),
    }

    # =================================================================
    #
    return render(request, "profile.html", context)
    return render(request, "user_profile.html", context)


# class CustomLoginView(LoginView):

#     def post(self, request):
#         print(request.GET, "<<<<<<< ========")
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
#                 f"/user/{username}"
#                 # f"/user/"
#             )  # Замените 'home' на имя вашего URL-шаблона для главной страницы
#         else:
#             # Если аутентификация не удалась, показать ошибку входа
#             return render(
#                 request,
#                 "login.html",
#                 {"error_message": "Неправильный логин или пароль"},
#             )


# def answer(request, question_id):
#     """Ответ на вопрос"""
#     username = request.user
#     print(username)
#     try:
#         if request.method == "POST":
#             autor_obj = User.objects.get(username=username)
#             question_obj = Question.objects.get(id=question_id)
#             text = request.POST.get("message")
#             awnswer_add = Answer.objects.create(
#                 autor=autor_obj, question=question_obj, text=text
#             )
#             awnswer_add.save()

#         # return redirect(f"/user/{request.user}")
#         return redirect(f"/q/{question_id}")
#     except Exception as e:
#         print(e)
#         return render(request, "login.html")


@login_required(login_url="/login_in")
def create(request, **kwargs):

    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect("index")
    # form = QForm()
    form = QForm(initial={"autor": request.user})
    context = {"form": form}
    return render(request, "main/create_qust_form.html", context)


# def logoutPage(request):
#     logout(request)
#     return redirect("index")
