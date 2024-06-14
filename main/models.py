from datetime import timedelta
import uuid

from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser
from .settings import CACH_UPDATE_MIN

from PIL import Image as PilImage


class Teg(models.Model):
    name = models.CharField(max_length=10)

    # @property
    def __str__(self):
        return self.name


class User(AbstractUser):
    # REQUIRED_FIELDS = ["email", "username", "password"]
    profession = models.CharField(max_length=50, default="", blank=True)
    rating_cache = models.IntegerField(default=-1)
    rating_cache_updated_at = models.DateTimeField(auto_now_add=True)
    #
    image_url = models.CharField(max_length=50, blank=True, editable=False)

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
    # teg = models.CharField(max_length=10, blank=False)
    tegs = models.ForeignKey(
        Teg, on_delete=models.SET_NULL, null=True, blank=True, related_name="tegs_set"
    )
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

    from django.db import models


def user_directory_path(instance, filename) -> str:
    return "static/profile/picture/{0}/{1}".format(uuid.uuid4(), "file-1.jpg")


class Image(models.Model):
    user = models.ForeignKey(User, related_name="images_user", on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=user_directory_path, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:

            super().save(
                *args, **kwargs
            )  # Сначала сохраните изображение, чтобы получить доступ к полю `image`

            if self.image:
                img = PilImage.open(self.image.path)

                # Измените размер изображения
                max_size = (128, 128)
                img.thumbnail(max_size, PilImage.Resampling.LANCZOS)

                img.save(self.image.path)
        except Exception as e:
            return e
        # Image.objects.all().delete()
        # Image.objects.filter(id=self.id).delete()

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
