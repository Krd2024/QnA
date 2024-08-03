import math
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from main.models import (
    Notification,
    Question,
    Answer,
    Rection,
    Subscription,
    Teg,
    User,
    Image,
)
from main.forms import ProfileEditForm
from django.db.models import Count
from django.shortcuts import render


# =================================================================

from django.shortcuts import render, redirect


def get_notification(request, **kwargs):
    """Показать все не прочитанные уведомления + изменить статус 'is_read'"""
    print(kwargs)

    # notific_all = get_notifications_for_user(request.user.id)

    notific_all = Notification.objects.filter(recipient=request.user, is_read=False)
    for noti in notific_all:
        print(f"{noti.notification_type}:{noti.sender}")
    if kwargs.get("read") == str(1):
        for noti in notific_all:
            noti.is_read = True
            noti.save()

    elif kwargs.get("read") == str(0):
        notific_all = Notification.objects.filter(recipient=request.user)

        for noti in notific_all:

            noti.is_read = False
            noti.save()

    context = {
        "notific_all": notific_all,
    }
    return render(
        request,
        "notification.html",
        context,
    )


def user_profile(request, *args, **kwargs):
    """Профиль пользователя"""

    try:
        user = kwargs["username"]
        objects_user = User.objects.get(username=user)
    except Exception as e:
        print(e, "<< ------ def user_profile():")
        return redirect("index")

    if request.GET.get("q") == "questions":
        user_question = Question.objects.filter(autor=objects_user)
        context = {
            "user_question": user_question,
        }
        return render(request, "user_questions.html", context)

    objects_user = User.objects.get(username=user)
    user_question = Question.objects.filter(autor=objects_user)
    answers = Answer.objects.filter(autor=objects_user)

    if request.GET.get("q") == "answers":

        try:
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

            answer_obj = Answer.objects.get(id=answer_id)
            print(answer_obj.autor)
            print(answer_obj.id)
            try:
                obj = Notification.objects.filter(
                    # sender=request.user,
                    # sender=answer_obj.autor,
                    # notification_type="answer",
                    related_object_id=answer_obj.id,
                ).delete()

            except Exception as e:
                print(e, "<<< ----- e")
            answer_obj.delete()
            return redirect(f"/user/{request.user}/")

    except Exception as e:
        print(e, "< === def answer_update_delete(request, **kwargs):")
        return redirect(f"/user/{request.user}/")
