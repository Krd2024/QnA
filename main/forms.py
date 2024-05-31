from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Question, User


# class QForm(BaseModelForm):
class QForm(ModelForm):

    class Meta:
        model = Question
        exclude = []
        # fields = ("autor", "teg", "title", "text", "id")
        fields = "__all__"
        widgets = {"id": forms.HiddenInput()}


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class QuestionForm(forms.Form):
    question = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4, "cols": 40}), label="Your Question"
    )


from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""

    class Meta:
        model = Image
        fields = ("title", "image")
