from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.models import Question, Answer
from django.contrib.auth.models import User
from .forms import QForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required


def answer_update_delete(request, **kwargs):

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

    # answer_id = kwargs.get("username")
    # update_answer_obj = Answer.objects.get(id=27)
    # question_obj = Question.objects.get(id=1)
    # context = {"quest": question_obj, "answer": update_answer_obj}
    # return render(request, "questions.html", context)


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
        # Answer.objects.filter(question__in=other_questions)
        Answer.objects.all()
        .values("question_id")
        .annotate(total=Count("question_id"))
    )
    # user = User.objects.get(username="Den")
    all_question = Question.objects.all()

    context = {
        "all_question": all_question,
        "answers": answers,
    }
    return render(request, "main/index_main.html", context)


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
        form = QForm(
            initial={"text": question_obj[0].text, "autor": question_obj[0].autor}
        )
        context = {"form": form}
        return render(request, "main/update_qust_form.html", context)


def delete(request, **kwargs):
    # print(kwargs.get("name"), "---1")
    try:
        Question.objects.filter(id=kwargs["question_id"]).delete()
        return redirect(f"/user/{request.user}/")
    except Exception as e:
        print(e)
    return render(request, "profile.html")


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
            try:
                proverka_na_dublic = Answer.objects.filter(
                    autor=autor_obj, question=question_obj
                )
                proverka_na_dublic.delete()
                print(len(proverka_na_dublic))
            except Exception as e:
                print(e, "<<<< ======== E")

            text = request.POST.get("message")
            answer_add = Answer.objects.create(
                autor=autor_obj, question=question_obj, text=text, correct=0
            )
            answer_add.save()
            print("дошло до сохранения")
            return redirect("question", kwargs["question_id"])

        context = {"quest": question_obj}
        print("дошло до ..........")
        return render(request, "questions.html", context)
        return redirect(f"/user/{request.user}/")
    except Exception as e:
        print(e, "<<< (e) def question(request, **kwargs)")
        return HttpResponse("err")


# def login_in(request):
#     return render(request, "login.html")


def user_profile(request, *args, **kwargs):

    user = kwargs["username"]
    print(request.user.username, "<<< request user")
    print(user, "<<< user")
    print(request.GET.get("q"))

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

            if request.user.username == user:
                print("ravno")
                return render(request, "user_answers.html", context)
            else:
                print("ne ravno")
                return render(request, "user_answers_kostil.html", context)

        except Exception as e:
            print(e)
            return render(render, "user_answers.html", {"out": "Нет ответ"})

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
    return render(request, "profile.html", context)


@login_required(login_url="/login_in")
def create(request, **kwargs):

    if request.method == "POST":
        print(request.POST)
        form = QForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(f"/user/{request.user}/")
    # form = QForm()
    form = QForm(initial={"autor": request.user})
    context = {"form": form}
    return render(request, "main/create_qust_form.html", context)
