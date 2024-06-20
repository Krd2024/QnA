from django.db.models import Count, OuterRef, Subquery

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from main.models import Question, Answer, Rection, Subscription, Teg, User, Image
from .forms import ProfileEditForm, QForm, UserRegisterForm
from django.db.models import Count
from django.shortcuts import render


import os
import shutil

import time
from datetime import datetime
import main.settings
from django.contrib import messages

# =================================================================

from django.shortcuts import render, redirect

from bs4 import BeautifulSoup
import requests


def add_tag(request):
    print("tag add")
    try:
        tag_id = request.GET.get("tag_id")
        subscr = Subscription.objects.filter(tag=tag_id, user=request.user)
        tag_obj = Teg.objects.filter(id=tag_id)[0]
        if not subscr.exists():
            Subscription.objects.create(user=request.user, tag=tag_obj)
            return JsonResponse({"success": True, "answer": 1})
        else:
            Subscription.objects.filter(user=request.user, tag=tag_obj).delete()
            return JsonResponse({"success": True, "answer": -1})
    except Exception as e:
        print(e)
    return redirect("tegs")


# =================================================================
def questions_in_tag(request, **kwargs):
    """Показать вопросы по тегу"""
    try:
        page = request.GET.get("page", 1)
        start_time_1 = time.perf_counter_ns()
        #
        answers = (
            Answer.objects.all()
            .values("question_id")
            .annotate(total=Count("question_id"))
        )
        #
        end_time_1 = time.perf_counter_ns()
        execution_time_ns_1 = end_time_1 - start_time_1
        total_time_ms_1 = execution_time_ns_1 / 1_000_000_000
        print(f"Время получения кол-во ответов: {total_time_ms_1:.4f} seconds")
        #
        start_time_1 = time.perf_counter_ns()
        #
        all_question = Question.objects.filter(
            tegs=Teg.objects.filter(name=kwargs.get("tegs")).first()
        )
        # ----------------------------------------------------------------
        end_time_1 = time.perf_counter_ns()
        execution_time_ns_1 = end_time_1 - start_time_1
        total_time_ms_1 = execution_time_ns_1 / 1_000_000_000
        print(f"Время получения вопросов: {total_time_ms_1:.4f} seconds")
        #  ----------------------------------------------------------------
        # all_question = Question.objects.all().filter(tegs=kwargs.get("tegs"))
        num_pages = int(
            math.ceil(len(all_question) / main.settings.LIMIT_OF_USERS_ON_PAGE)
        )
        users_per_page = main.settings.LIMIT_OF_USERS_ON_PAGE
        paginator = Paginator(all_question, users_per_page)  # Создаем пагинатор

        try:
            sorted_users = paginator.page(page)
        except PageNotAnInteger:
            sorted_users = paginator.page(1)
        except EmptyPage:
            sorted_users = paginator.page(paginator.num_pages)

        context = {
            "page_number": page,
            "pages_range": range(1, num_pages + 1),
            "all_question": sorted_users,
            "answers": answers,
        }
    except Exception as e:
        print(e, "< ----- def questions_in_tag(): ")
        return redirect("index")

    return render(request, "main/index_main.html", context)
    #
    #


def tegs(request):
    """Показать все теги"""
    # autor = User.objects.get(id=random.randint(50, 1629))
    # print(autor)
    start_time_0 = time.perf_counter_ns()
    try:
        tegs = {}
        tegs_obj = Teg.objects.prefetch_related("tegs_set").all()

        for teg in tegs_obj:
            # tag_dict = teg.tag_subscription
            # print(f"Название тега: {teg.name}")
            quest = teg.tegs_set.all()
            questions = []
            for related in quest:
                questions.append(related.text)
                # print(f"Вопросы связанные с тегом: {related.text}")
            tegs[teg.name] = questions
        end_time_0 = time.perf_counter_ns()

        execution_time_ns = end_time_0 - start_time_0
        execution_time_s = execution_time_ns / 1_000_000_000
        print(f"Время выполнения Тег-вопросы: {execution_time_s:.4f} секунд")

        #  ==================  Подписки =============================================
        start_time_1 = time.perf_counter_ns()

        data = Subscription.objects.select_related("user", "tag").all()

        tag_dict = {}

        for entry in data:

            user = entry.user
            tag = entry.tag
            # Если тег еще не существует в словаре, создаем для него пустой список
            if tag not in tag_dict:
                tag_dict[tag] = []

            #     # Добавляем пользователя в список значений соответствующего тега
            tag_dict[tag].append(user)

        end_time_1 = time.perf_counter_ns()

        execution_time_ns = end_time_1 - start_time_1
        execution_time_s = execution_time_ns / 1_000_000_000
        print(f"Время выполнения  Тег-подписчики: {execution_time_s:.4f} секунд")

        # # Выводим результат
        # for tag, users in tag_dict.items():
        #     print(f"{tag}: {users}")

        # print(tag_dict)

        # Получение имени тега и количества пользователей, подписанных на него
        # tags_with_user_count = Teg.objects.annotate(user_count=Count("subscriptions"))
        # subscription = Subscription.objects.all()
        # user_tegs = {}
        # for tag in tags_with_user_count:
        #     user_tegs[tag.name] = tag.user_count
        #     print(f"Tag: {tag.name}, User Count: {tag.user_count}")
        #     print(tag)
        # print(user_tegs)

        #  ==========================================================================
        return render(
            request,
            "all_tegs.html",
            {"tegs": tegs, "tag_dict": tag_dict},
        )

    except Exception as e:
        print(e, "< ------------ def tegs(request)")
    return redirect("index")


def pars_up(request, **kwargs):
    print(kwargs)
    try:
        if kwargs.get("value") == "samoe":

            url = "http://qna.habr.com/"
            page = requests.get(url)
            if page.status_code != 200:
                return False
            soup = BeautifulSoup(page.text, "html.parser")
            allNews = soup.findAll("li", class_="content-list__item")
            links = {}
            for news_item in allNews:
                link = news_item.find(
                    "a", class_="question__title-link question__title_thin"
                )
                if link:
                    text = " ".join(link.text.split()).strip()
                    links[text] = link["href"]
            return render(request, "wrapper/right_pars.html", {"links": links})

        elif kwargs.get("value") == "it":
            url = "http://habr.com/ru/news/"
            page = requests.get(url)
            if page.status_code != 200:
                return False
            soup = BeautifulSoup(page.text, "html.parser")
            allNewsIt = soup.findAll("article", class_="tm-articles-list__item")
            links = {}

            for news_item in allNewsIt:
                h2 = news_item.find("h2", class_="tm-title tm-title_h2")
                a = news_item.find("a", class_="tm-title__link")

                url = a["href"]
                link = f"HTTPS://habr.com{url}"
                text = h2.text
                links[text] = link
            return render(request, "wrapper/right_pars.html", {"links": links})

        elif kwargs.get("value") == "yandex":
            url_1 = "https://market.yandex.ru/"

            page = requests.get(url_1)
            if page.status_code != 200:
                return False

            soup = BeautifulSoup(page.text, "html.parser")
            allNews = soup.findAll("div", class_="_2rw4E _14Y_C")
            links1 = {}
            for news_item in allNews:

                link = news_item.find(
                    "h3", class_="G_TNq _2SUA6 _33utW IFARr _2a1rW _1A5yJ"
                )
                link2 = news_item.find("span", class_="_3gYEe")
                #   ==========================================================
                link3 = news_item.find("img", class_="_2Tepm")
                photograph = (
                    link3["src"] if link3["src"].startswith("https://avatars") else ""
                )
                #  ============================================================

                if link:
                    text1 = " ".join(link.text.split()).strip()
                    print(text1)
                    print("--------------------------------")
                    # links[text] = link["href"]
                if link2:
                    text2 = " ".join(link2.text.split()).strip()
                    print(text2)
                    print("================================")
                links1[text1] = text2

            return render(request, "wrapper/right_pars.html", {"links1": links1})

    except Exception as e:
        print(e)
        return redirect("index")

    # return render(request, "wrapper/right_pars.html", {"links": links})


# =================================================================
def edit_profile(request, **kwargs):
    if request.method == "POST":
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            form.save(commit=False)

            first = form.cleaned_data["first_name"]
            last = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            pro = form.cleaned_data["profession"]

            edit_user = User.objects.get(pk=request.user.id)
            if first != "":
                edit_user.first_name = first
            if last != "":
                edit_user.last_name = last
            if email != "":
                edit_user.email = email
            if pro != "":
                edit_user.profession = pro
            edit_user.save()

            return redirect("user_profile", request.user.username)
            # return HttpResponse(1)

        print()
    form = ProfileEditForm

    return render(request, "editProfile.html", {"form": form})


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
def all_users(request, **kwargs):
    """Показать всех пользователей"""
    start_time_0 = time.perf_counter_ns()
    try:
        question_count_subquery = (
            Question.objects.filter(autor=OuterRef("pk"))
            .values("autor")
            .annotate(count=Count("*"))
            .values("count")
        )
        answer_count_subquery = (
            Answer.objects.filter(autor=OuterRef("pk"))
            .values("autor")
            .annotate(count=Count("*"))
            .values("count")
        )

        # Выполните аннотированный запрос
        users_obj_count = User.objects.annotate(
            question_count=Subquery(question_count_subquery),
            answer_count=Subquery(answer_count_subquery),
        )
    except Exception as e:
        print(e, "< --------- all users")

    end_time_0 = time.perf_counter_ns()

    execution_time_ns = end_time_0 - start_time_0
    execution_time_s = execution_time_ns / 1_000_000_000
    print(f"Время выполнения запроса к базе: {execution_time_s:.4f} секунд")

    # users_obj_count = User.objects.annotate(
    #     question_count=Count("question_set"), answer_count=Count("answer_set")
    # )

    # for user in users_obj_count:
    #     print(user.answer_count, " ", user.question_count)

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

    start_time_1 = time.perf_counter_ns()

    users_per_page = (
        main.settings.LIMIT_OF_USERS_ON_PAGE
    )  # Ограничение пользователей на странице

    # Сортировка и пагинация с использованием ORM
    users_obj_pag = User.objects.order_by(
        "-rating_cache"
    )  # Сортируем по рейтингу по убыванию
    paginator = Paginator(users_obj_pag, users_per_page)  # Создаем пагинатор

    try:
        sorted_users = paginator.page(page)
    except PageNotAnInteger:
        sorted_users = paginator.page(1)
    except EmptyPage:
        sorted_users = paginator.page(paginator.num_pages)

    # sorted_users = sorted(users_obj, key=lambda u: u.rating, reverse=True)
    # sorted_users = sorted_users[
    #     (page - 1)
    #     * main.settings.LIMIT_OF_USERS_ON_PAGE : (page)
    #     * main.settings.LIMIT_OF_USERS_ON_PAGE
    users_obj = User.objects.all()
    num_pages = int(math.ceil(len(users_obj) / main.settings.LIMIT_OF_USERS_ON_PAGE))

    end_time_1 = time.perf_counter_ns()
    execution_time_ns_1 = end_time_1 - start_time_1
    total_time_ms_1 = execution_time_ns_1 / 1_000_000_000
    print(
        f"Время выполнения сортировки страниц в представлении: {total_time_ms_1:.4f} seconds"
    )

    start_time = time.time()

    response = render(
        request,
        "all_users.html",
        {
            "users": sorted_users,
            "pages_range": range(1, num_pages + 1),
            "page_number": page,
            # "count_answer_users": count_answer_users,
            # "count_questions_users": count_questions_users,
            "users_obj_count": users_obj_count,
        },
    )
    end_time = time.time()
    total_time = end_time - start_time
    total_time_ms = total_time / 1_000_000_000
    print(f"Template render time: {total_time_ms:.4f} seconds")

    return response


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


# @type_
def search(request, **kwargs):
    """Поиск по заголовку и тегу"""

    print(kwargs["search"])

    try:
        search = kwargs["search"]
        # print(search, "<<<<<<<<<<<<<<<<<<<<<<")
        question = Question.objects.all()
        tegs = Teg.objects.all()
        title_question = {}

        for title in question:
            title_question[title.id] = title.title.split(" ")

        for key, val in title_question.items():
            if search in val:
                sentence = " ".join(val)
                # print(sentence)
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


def index(request):
    answers = (
        Answer.objects.all().values("question_id").annotate(total=Count("question_id"))
    )
    # ИСПРАВИТЬ
    all_question = Question.objects.all()[:]

    context = {
        "all_question": all_question,
        "answers": answers,
    }
    return render(request, "main/index_main.html", context)


def user_profile(request, *args, **kwargs):

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
            return render(render, "user__answers.html", {"out": "Нет ответ"})
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


# t = Teg.objects.all()
#     for i in t:
#         i.name = i.name.replace("#", "").replace(",", "").replace('"', "")
#         i.save()
