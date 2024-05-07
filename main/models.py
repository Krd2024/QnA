from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


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


class Answer(models.Model):
    autor = models.ForeignKey(
        User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="answer_set",
    )
    question = models.ForeignKey(
        User,
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


class Rection(models.Model):
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
    answer = models.ForeignKey(
        Answer, null=True, blank=False, on_delete=models.SET_NULL
    )
    value_yes = models.SmallIntegerField()
    value_no = models.SmallIntegerField()
