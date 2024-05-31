from datetime import timedelta

from django.utils import timezone

import time
from django.db import models
from django.contrib.auth.models import AbstractUser
from .settings import CACH_UPDATE_MIN

# class AppUser()


class User(AbstractUser):
    # REQUIRED_FIELDS = ["email", "username", "password"]
    profession = models.CharField(max_length=50, default="", blank=True)
    rating_cache = models.IntegerField(default=-1)
    rating_cache_updated_at = models.DateTimeField(auto_now_add=True)

    @property
    def rating(self):
        if (
            self.rating_cache_updated_at + timedelta(minutes=CACH_UPDATE_MIN)
            < timezone.now()
        ):
            answer_true = Answer.objects.filter(autor=self, correct=True).count() * 10
            reaction_count = Rection.objects.filter(user=self).count() * 3

            self.rating_cache = answer_true + reaction_count
            self.rating_cache_updated_at = timezone.now()
            self.save()

        return self.rating_cache


class Question(models.Model):
    autor = models.ForeignKey(
        User,
        max_length=20,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="question_set",
    )
    teg = models.CharField(max_length=10, blank=False)
    title = models.CharField(max_length=50, blank=False)
    text = models.TextField(max_length=200, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    views = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title

    @property
    def answers(self):
        return Answer.objects.filter(question=self).order_by("-created_at")


class Answer(models.Model):
    autor = models.ForeignKey(
        User,
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name="answer_set",
    )
    question = models.ForeignKey(
        Question,
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name="question",
    )

    text = models.TextField(max_length=20, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    parent = models.ForeignKey(
        "self", null=True, blank=False, on_delete=models.SET_NULL
    )
    correct = models.BooleanField(default=False, blank=True)

    def __str__(self) -> str:
        q = Question.objects.get(id=self.question.id)
        return f"Вопрос ' _ {q} _ ': {self.text}"


class Rection(models.Model):
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
    answer = models.ForeignKey(
        Answer,
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name="rection_set",
    )
    value = models.IntegerField(default=0)

    # @property
    # def reaction_count(self):
    #     return self.answer.count()

    # class rangs(models.Model):

    #     def __init__(self, username):
    #         self.username = username
    #         self.answer_count = Answer.objects.filter(user=username)
    #         self.reaction_count = Rection.objects.filter(user=username)

    #     def get_rangs(self):
    #         ans = self.answer_count
    #         rec = self.reaction_count
    #         return len(ans), len(rec)

    # @property
    # def answers(self):
    # return Answer.objects.filter(question=self).order_by("-created_at")

    """
    поля класса User 
username: Имя пользователя (username).
password: Пароль.
email: Электронная почта.
first_name: Имя.
last_name: Фамилия.
is_active: Флаг, показывающий, активен ли пользователь.
is_staff: Флаг, указывающий, имеет ли пользователь доступ к административному интерфейсу.
is_superuser: Флаг, указывающий, является ли пользователь суперпользователем.
date_joined: Дата и время регистрации пользователя.
    """
