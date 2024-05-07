from django.shortcuts import render
from main.models import Question, Answer, Rection, UserProfile, User

# from django.contrib.auth.models import User


def index(request):
    user = User.objects.get(username="Den")
    # print(user)
    count = 0
    all_question = Question.objects.all()
    for question in all_question:
        print(question.autor, ": ", count)
        count += 1
        context = {"all_question": all_question}

    return render(request, "index.html", context)


def q(request, id_question):
    print(id_question)
    question = Question.objects.filter(id=id_question)
    context = {"question": question}

    return render(request, "questions.html", context)


def user(request):
    return render(request, "index.html")


def info(request, username):
    print(username)

    return render(request, "index.html")


def gg(request):
    user = User.objects.get(username="Sem")
    lst_q = [
        "Какие основные методы для работы со строками существуют в Python?",
        "Что такое исключения (exceptions) в Python, и как их обрабатывать?",
        "Как создать функцию (def) в Python, и как передать ей аргументы?",
        "Чем отличаются методы `append()` и `extend()` для списка в Python?",
        "Каким образом можно выполнить чтение и запись данных в файле в Python?",
    ]
    for item in lst_q:
        zapis = Question.objects.create(autor=user, title="Python", text=item)
        zapis.save()
    return render(request, "index.html")
