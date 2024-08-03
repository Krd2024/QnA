from datetime import datetime, timedelta
import datetime
import uuid

from django.forms import JSONField
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser
from .settings import CACH_UPDATE_MIN, CACH_UPDATE_TAGS_MIN

from PIL import Image as PilImage


class Subscription(models.Model):
    # subscr_cache_updated_at = models.DateTimeField(default=datetime.datetime.now)
    subscr_cache_updated_at = models.DateTimeField(auto_now_add=True)

    tag = models.ForeignKey(
        "Teg",
        related_name="subscriptions",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )
    user = models.ForeignKey(
        "User",
        related_name="subscriptions",
        null=True,
        on_delete=models.SET_NULL,
    )
    # tag_dict = models.JSONField()

    def update_cache(self):
        data = Subscription.objects.all()
        tag_dict_user = {}

        for entry in data:
            user = entry.user.username  # Предполагая, что User имеет поле 'username'
            tag = entry.tag.name  # Предполагая, что Teg имеет поле 'name'

            if tag not in tag_dict_user:
                tag_dict_user[tag] = []

            tag_dict_user[tag].append(user)

        self.subscr_cache_updated_at = timezone.now()

        self.save()

    @property
    def tag_subscription(self):
        # if (
        #     self.subscr_cache_updated_at + timedelta(minutes=CACH_UPDATE_TAGS_MIN)
        #     < timezone.now()
        # ):
        self.update_cache()

        return self.tag_dict

    # def user_collection_tegs(self, user):
    #     collec_obj = Subscription.objects.filter(user=user)
    #     return collec_obj

    class Meta:
        unique_together = ("tag", "user")


class Teg(models.Model):
    name = models.CharField(max_length=10)
    tags_questions = JSONField()
    # tags_user_count_cache = models.IntField()
    # tags_user_count_cache = models.IntField()

    # @property
    # def tags_user_count(self):
    #     from django.db.models import Count

    #     tags_with_user_count = Teg.objects.annotate(user_count=Count("subscriptions"))
    #     return tags_with_user_count

    @property
    def tag_questions(self):
        try:
            tegs = {}
            tegs_obj = Teg.objects.prefetch_related("tegs_set").all()

            for teg in tegs_obj:
                # print(f"Название тега: {teg.name}")
                quest = teg.tegs_set.all()
                questions = []
                for related in quest:
                    questions.append(related.text)
                    # print(f"Вопросы связанные с тегом: {related.text}")
                tegs[teg.name] = questions

            return tegs

        except Exception as e:
            print(e)

        # Выводим результат
        # for tag, users in tag_dict.items():
        #     print(f"{tag}: {users}")

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


# from django.db import models
# from django.contrib.auth.models import User


class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ("like", "Like"),
        ("answer", "Answer"),
    )

    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications_sent"
    )  # от кого

    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications_received"
    )  # кому
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    related_object_id = models.PositiveIntegerField()

    class Meta:
        ordering = ["-created_at"]

        unique_together = (
            "notification_type",
            "related_object_id",
            "sender",
            "recipient",
        )

    def __str__(self):
        return f"{self.get_notification_type_display()} для {self.recipient.username}"

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
