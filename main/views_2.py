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


def question(request, **kwargs): ...
