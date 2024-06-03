import math
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from main.models import Question, Answer, Rection, User, Image
from .forms import QForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ImageForm, ProfileEditForm

import os
import shutil

import time
from datetime import datetime
import main.settings
from django.contrib import messages

# =================================================================
# views.py

from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRegisterForm


# =================================================================
def edit_profile(request, **kwargs):
    if request.method == "POST":
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["first_name"])
            print(form.cleaned_data["last_name"])

            user=form.save(commit=False)
            return redirect("user_profile", request.user)
            # return HttpResponse(1)

        print()
    form = ProfileEditForm

    return render(request, "editProfile.html", {"form": form})


# from django.contrib.auth.models import User


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
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


# =================================================================
# =================================================================
#                 НЕ ИСПОЛЬЗУЕТСЯ
import uuid


def generate_filename(instance, filename):
    # Получить расширение файла
    extension = os.path.splitext(filename)[1]
    # Генерировать уникальное имя файла с помощью uuid
    new_filename = str(uuid.uuid4()) + extension
    # Вернуть путь для сохранения файла
    return os.path.join("static", "profile", "picture", new_filename)


# =================================================================


def delete_folder(folder_path):
    """Удалить текущую папку uuid перед созданием новой"""
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Папка '{folder_path}' успешно удалена.")
    else:
        print(f"Папка '{folder_path}' не существует.")


def image_upload_view(request):
    """Загрузка фото пользователя"""

    def save_image_url_user(img_obj):
        User.objects.filter(
            username=request.user.username,
        ).update(image_url=str(img_obj)[23:59])

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img_obj = Image.objects.filter(user_id=request.user)
            if img_obj is not None:
                img_obj.delete()

            image = form.save(commit=False)
            image.user = request.user
            image.save()

            img_obj = form.instance
            #
            print(form.cleaned_data["image"])
            #
            if form.cleaned_data["image"] is None:
                return render(request, "load_img.html", {"form": form})

            # Получить имя папки для удаления перед созданием новой (uuid)
            user_obj = User.objects.filter(username=request.user.username).first()
            dir_uuid = user_obj.image_url
            print(dir_uuid, "<<<<<< ---------- user_obj")

            if dir_uuid == "":
                save_image_url_user(img_obj.image)
                return redirect("user_profile", request.user.username)

            folder_path = f"static/profile/picture/{dir_uuid}"
            delete_folder(folder_path)

            save_image_url_user(img_obj.image)
            #
        return redirect("user_profile", request.user.username)
    else:
        form = ImageForm()
    return render(request, "load_img.html", {"form": form})


# ======================================================
def all_users(request, **kwargs):
    """Показать всех пользователей"""
    # ======================================================
    answer_obj_1 = Rection.objects.select_related("answer")
    for obj in answer_obj_1:
        print(obj.answer.text)
    # ======================================================

    answer_obj = Answer.objects.prefetch_related("rection_set")
    for answer in answer_obj:
        ans_react = answer.rection_set.all()
        for related in ans_react:
            print(related.user)
    # ======================================================
    # ======================================================

    page = kwargs.get("page")
    if page is not None:
        try:
            page = int(page)
            if page < 2:
                raise ValueError()
        except:
            return redirect("all_users")
    else:
        page = 1

    users_obj = User.objects.all()

    sorted_users = sorted(users_obj, key=lambda u: u.rating, reverse=True)
    sorted_users = sorted_users[
        (page - 1)
        * main.settings.LIMIT_OF_USERS_ON_PAGE : (page)
        * main.settings.LIMIT_OF_USERS_ON_PAGE
    ]

    num_pages = int(math.ceil(len(users_obj) / main.settings.LIMIT_OF_USERS_ON_PAGE))
    users_obj = users_obj

    count_answer_users = {}
    count_questions_users = {}

    try:

        for user in users_obj:
            question_obj = Question.objects.filter(autor=user)
            answers_obj = Answer.objects.filter(autor=user)
            #
            count_answer_users[user] = len(answers_obj)
            count_questions_users[user] = len(question_obj)

    except Exception as e:
        print(e, "<<< e -------------- def all_users(request)")

    return render(
        request,
        "all_users.html",
        {
            "users": sorted_users,
            "pages_range": range(1, num_pages + 1),
            "page_number": page,
            "count_answer_users": count_answer_users,
            "count_questions_users": count_questions_users,
        },
    )


def rating(request):
    text = """ Как увеличивается вклад пользователя
            Его ответ принят как решение: +10 очков
            Его ответ нравится: +3 очка """
    return HttpResponse(text)


def correct(request, **kwargs):
    """Поставить отметку ответу 'корректный'"""
    if not request.user.is_authenticated:
        return HttpResponse()
    if request.method == "POST":
        answer_id = kwargs["answer_id"]
        answer_obj = Answer.objects.get(id=answer_id)
        if (
            request.user != answer_obj.question.autor
            or answer_obj.autor == request.user
        ):
            return HttpResponse()

        new_correct = Answer.objects.get(id=answer_id)
        new_correct.correct = True
        new_correct.save()

    return JsonResponse({"success": True, "a": f"good-answer"})


# ======================================================
def type_(search):
    """Без особого смысла"""

    def wrapper(*args, **kwargs):
        res1 = search(*args, **kwargs)
        if not isinstance(res1, (int)):
            return res1
        return 0

    return wrapper


# ======================================================


@type_
def search(request, **kwargs):
    """Поиск по заголовку"""

    print(kwargs["search"])

    try:
        search = kwargs["search"]
        print(search, "<<<<<<<<<<<<<<<<<<<<<<")
        question = Question.objects.all()
        title_question = {}

        for title in question:
            title_question[title.id] = title.title.split(" ")

        for key, val in title_question.items():
            if search in val:
                sentence = " ".join(val)
                print(sentence)
                return HttpResponse(key)
        return HttpResponse()

    except Exception as e:
        print(e, "<<<< ------------- E --- def search()")
    return render(request, "question.html")


def increase_counter(request, **kwargs):
    """Поставить,убрать like"""

    print("пришло")
    if not request.user.is_authenticated:
        return HttpResponse()
    answer_id = kwargs.get("answer_id")
    if request.method == "POST":
        try:
            answer = Answer.objects.get(id=answer_id)

            proverka = Rection.objects.filter(answer=answer, user=answer.autor)
            if len(proverka) != 0:
                proverka.delete()
                reac_count = answer.rection_set.count()
                return JsonResponse({"success": True, "answer": reac_count})
            elif request.user == answer.autor:
                return HttpResponse()

            reaction = Rection.objects.create(answer=answer, user=answer.autor)
            reaction.save()
            reac_count = answer.rection_set.count()
            # print(reac_count)
            return JsonResponse({"success": True, "answer": reac_count})

        except Exception as e:
            print(e)
    return HttpResponse()


def answer_update_delete(request, **kwargs):
    """Редактировать,удалить ответ"""

    try:
        data = kwargs.get("choice")
        answer_id = kwargs.get("answer_id")

        if data == "ans_update":
            answer_obj = Answer.objects.get(id=answer_id)
            context = {"quest": answer_obj.question, "answer": answer_obj.text}
            return render(request, "questions.html", context)

        elif data == "ans_delete":
            answer_obj = Answer.objects.get(id=answer_id).delete()
            return redirect(f"/user/{request.user}/")

    except Exception as e:
        print(e, "< === def answer_update_delete(request, **kwargs):")
        return redirect(f"/user/{request.user}/")


def info_user_choice(request, **kwargs):
    """Получить все вопросы или все ответы пользователя для ЛК"""

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

        if kwargs.get("choice") == "answer":
            username = kwargs.get("name")
            print(username, "<<< ======= username")
            user_obj = User.objects.get(username=username)
            user_answer_obj = Answer.objects.filter(autor=user_obj)

            context = {"user_answer": user_answer_obj, "answers": len(user_answer_obj)}
            return render(request, "profile.html", context)
            # return render(request, "user_info.html", context)

    except Exception as e:
        print(e, "<< --- E")
    return HttpResponse("errrror << --- def(info_user_choice)")


def info_user(request, **kwargs):
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
        Answer.objects.all().values("question_id").annotate(total=Count("question_id"))
    )
    all_question = Question.objects.all()

    context = {
        "all_question": all_question,
        "answers": answers,
    }
    return render(request, "main/index_main.html", context)


def update(request, **kwargs):
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
        form = QForm(
            initial={"text": question_obj[0].text, "autor": question_obj[0].autor}
        )
        context = {"form": form}
        return render(request, "main/update_qust_form.html", context)


def delete(request, **kwargs):
    try:
        Question.objects.filter(id=kwargs["question_id"]).delete()
        return redirect(f"/user/{request.user}/")
    except Exception as e:
        print(e)
    return render(request, "profile.html")


def question(request, **kwargs):
    """Выводит один вопрос и ответы к нему"""
    # ----------------------------------------------------------------
    question_obj = Question.objects.get(id=kwargs["question_id"])
    # ----------------------------------------------------------------
    print(kwargs, "<<<< ---------- kwargs ----------")
    try:
        question_obj = Question.objects.get(id=kwargs["question_id"])
        print(question_obj, "<<<< ---------- question_obj ----------")

        if request.method == "POST":
            if not request.user.is_authenticated:
                return redirect("login")

            autor_obj = User.objects.get(username=request.user)
            question_obj = Question.objects.get(id=kwargs["question_id"])
            try:
                proverka_na_dublic = Answer.objects.filter(
                    autor=autor_obj, question=question_obj
                )
                proverka_na_dublic.delete()
                print(
                    proverka_na_dublic,
                    " --- ",
                    len(proverka_na_dublic),
                    "<<<< ------------ proverka_na_dublic",
                )
            except Exception as e:
                print(e, "<<<< ======== E")

            text = request.POST.get("message")
            answer_add = Answer.objects.create(
                autor=autor_obj, question=question_obj, text=text, correct=0
            )
            answer_add.save()
            return redirect("question", kwargs["question_id"])
        # ---------------------------------------------
        answers = question_obj.answers.all()
        # Подсчет реакций для каждого ответа
        for answer in answers:
            answer.reaction_count = answer.rection_set.count()
        # --------------------------------------------
        context = {"quest": question_obj, "answers": answers}

        return render(request, "questions.html", context)
    except Exception as e:
        print(e, "<<< (e) def question(request, **kwargs)")
        return HttpResponse("err")


def user_profile(request, **kwargs):

    user = kwargs["username"]

    objects_user = User.objects.get(username=user)
    if request.GET.get("q") == "questions":
        # print(12345)
        user_question = Question.objects.filter(autor=objects_user)
        context = {
            "user_question": user_question,
        }

        return render(request, "user_questions.html", context)

    if request.GET.get("q") == "answers":
        try:
            answers = Answer.objects.filter(autor=objects_user)
            lst = []
            for answer in answers:
                lst.append(answer.question_id)

            question = Question.objects.filter(id__in=lst)
            context = {"question": question, "user": user}
            # ---------------------------------------------------------------------
            if len(answers) == 0:
                return HttpResponse("Нет ответ")
            return render(request, "user___answers.html", context)

        except Exception as e:
            print(e, "<<< ----------- e --- def user_profile()")
            return render(render, "user_answers.html", {"out": "Нет ответ"})
    # ----------------------------------------------------------------
    objects_user = User.objects.get(username=user)
    user_question = Question.objects.filter(autor=objects_user)
    answers = Answer.objects.filter(autor=objects_user)

    correct_answer = Answer.objects.filter(autor=objects_user, correct=True).count()

    # ----------------------------------------------------------------
    answers_1 = (
        Answer.objects.all().values("question_id").annotate(total=Count("question_id"))
    )

    context = {
        "user_question": len(user_question),
        "username": objects_user,
        "answers": len(answers),
    }

    return render(request, "profile.html", context)
    # =================================================================


@login_required(login_url="/login_in")
def create(request, **kwargs):

    def limit(request):
        try:
            user_id = request.POST.get("autor")
            user_obj = User.objects.get(id=user_id)
            question = Question.objects.filter(autor=user_obj)
            #
            current_time = time.time()
            dt_object = datetime.fromtimestamp(current_time)
            limit_time = dt_object.strftime("%Y-%m-%d")
            lst_time = []
            for i in question:
                str_time = i.created_at
                x = datetime.fromisoformat(str(str_time))
                time_question = x.strftime("%Y-%m-%d")
                if time_question == limit_time:
                    lst_time.append(time_question)
            # y = x.strftime("%Y-%m-%d %H:%M")
            print(len(lst_time))
            if len(lst_time) >= main.settings.MAX_QUESTIONS:
                print("Не части с вопросами")
                return True
            return False
        except Exception as e:
            print(e)
            messages.success(request, "На сегодня с вопросами всё")
            return redirect(f"/user/{request.user}/")

    if request.method == "POST":
        if limit(request):
            messages.success(request, "На сегодня с вопросами всё")
            return redirect(f"/user/{request.user}/")

        form = QForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(f"/user/{request.user}/")
    form = QForm(initial={"autor": request.user})
    context = {"form": form}
    return render(request, "main/create_qust_form.html", context)


# =================================================================


class EmployeeService:
    _model = "name_model"

    def add(self, **kwargs):
        return self._model.objects.create(**kwargs)

    def get_all(self):
        return self._model.objects.all()

    def get_by_id(self, pk: int):
        return self._model.objects.get(pk=pk)

    def delete_by_id(self, pk: int):
        employee = self._model.objects.get(pk=pk)
        return employee.delete()


service = EmployeeService()

# view.py
# from service import service
# ===========================================================
