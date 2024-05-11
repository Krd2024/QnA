from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.views import View

from main.models import Question, Answer, Rection
from django.contrib.auth.models import User
from .forms import QForm
from django.db.models import Count


from .forms import UserRegisterForm


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


def create(request, **kwargs):

    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect("index")

    form = QForm()
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
        question_obj = Question.objects.filter(id=kwargs["id_question"])
        context = {"question": question_obj, "username": objects_user}
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
    print(objects_user, "  <<<         obj_user")

    user_question = Question.objects.filter(autor=objects_user)
    other_questions = Question.objects.exclude(autor_id=objects_user)
    # answers = Answer.objects.filter(question__in=other_questions)
    # answers = Answer.objects.all()
    # print(answers, " <<< answer")
    # =================================================================
    """ 1-й Вариант """

    # answers_with_questions = Answer.objects.select_related("question").all()

    # print(answers_with_questions)
    # for answer in answers_with_questions:
    #     print(answer.question.id, "Ответ: ", answer.text)
    # =================================================================
    """ 2-й Вариант """

    # # Фильтрация объектов Answer по вопросам в other_questions и группировка по question_id
    answers = (
        # Answer.objects.filter(question__in=other_questions)
        Answer.objects.all()
        .values("question_id")
        .annotate(total=Count("question_id"))
    )
    # dict_ = {}
    # for answer in answers:
    #     question_id = answer["question_id"]
    #     total_count = answer["total"]
    #     dict_[question_id] = total_count
    #     print(f"для вопроса с id {question_id}: {total_count} ответа")

    # #
    context = {
        "user_question": user_question,
        "other_questions": other_questions,
        "username": objects_user,
        "answers": answers,
        #
        # "total_count": total_count,
        # "answers_with_questions": answers_with_questions,
        # "question_id":
    }
    # other_questions = list(other_questions.values())
    # #
    # for i in range(len(other_questions)):
    #     for k, v in other_questions[i].items():
    #         if k == "id" and v in dict_.keys():
    #             x = dict_.get(v)
    #             print(k, ":", v, "otvetov - ", x)
    #             context[str(v)] = x
    # print(context)
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
    # print(request.GET)
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
    return render(request, "answer.html")
