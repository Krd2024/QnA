from django.forms import BaseModelForm, ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Question, User


# class QForm(BaseModelForm):
class QForm(ModelForm):

    class Meta:
        model = Question
        fields = ("autor", "teg", "title", "text")
        # fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     autor = kwargs.pop("autor", None)  # Получаем значение autor из kwargs
    #     super(QForm, self).__init__(*args, **kwargs)
    #     if autor:
    #         self.initial["autor"] = autor


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
