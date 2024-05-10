from django.forms import BaseModelForm, ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Question, User


# class QForm(BaseModelForm):
class QForm(ModelForm):

    class Meta:
        model = Question
        fields = "__all__"


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
