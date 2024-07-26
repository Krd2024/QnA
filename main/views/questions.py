import math
from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.models import Notification, Question, Answer, Teg, User
from main.forms import ProfileEditForm, QForm, UserRegisterForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


import time
from datetime import datetime
import main.settings
from django.contrib import messages

# =================================================================

from django.shortcuts import render, redirect

from bs4 import BeautifulSoup
import requests


@login_required(login_url="/login_in")
def create(request, **kwargs):

    def limit(request):
        try:

            user_obj = User.objects.get(id=request.user.id)
            question = Question.objects.filter(autor=user_obj)
            print(user_obj)
            print(question)
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
            print(e, "<<< ---  def limit")
            messages.success(request, "На сегодня с вопросами всё")
            return redirect(f"/user/{request.user}/")

    if request.method == "POST":
        if limit(request):
            # messages.success(request, "На сегодня с вопросами всё")
            return redirect(f"/user/{request.user}/")

        form = QForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data["autor"]
            print(user)
            form.save()
        return redirect(f"/user/{request.user}/")
    form = QForm(initial={"autor": request.user})
    tegs = Teg.objects.all()
    context = {"form": form, "tegs": tegs}

    # context = {"form": form, "tegs": tegs}

    return render(request, "main/create_qust_form.html", context)


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

            # создать уведомление о создании ответа
            try:
                Notification.objects.create(
                    sender=request.user,
                    recipient=question_obj.autor,
                    notification_type="answer",
                    related_object_id=kwargs["question_id"],
                )
            except:
                ...

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
            question.tegs = form.cleaned_data["tegs"]
            print(question.tegs, "<<<< ======= tags")
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
