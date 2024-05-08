from django.db import models
from django.contrib.auth.models import User


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
    text = models.TextField(max_length=20, blank=False)
    created_at = models.DateField(auto_now_add=True, blank=False)
    updated_at = models.DateField(auto_now=True, blank=False)
    views = models.SmallIntegerField(default=0)

    def __str__(self) -> str:
        return self.title


class Answer(models.Model):
    autor = models.ForeignKey(
        User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="answer_set",
    )
    question = models.ForeignKey(
        Question,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="question",
    )

    text = models.TextField(max_length=20, blank=False)
    created_at = models.DateField(auto_now_add=True, blank=False)
    updated_at = models.DateField(auto_now=True, blank=False)
    parent = models.ForeignKey(
        "self", null=True, blank=False, on_delete=models.SET_NULL
    )
    correct = models.BooleanField(default=False, blank=True)

    def __str__(self) -> str:
        return self.text


class Rection(models.Model):
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
    answer = models.ForeignKey(
        Answer, null=True, blank=False, on_delete=models.SET_NULL
    )
    value = models.IntegerField()

    """
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
