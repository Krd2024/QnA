from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Image
from PIL import Image as PilImage

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

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False  # Делает аккаунт неактивным до подтверждения email
        if commit:
            user.save()
        return user


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

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            # Открываем изображение с помощью Pillow
            pil_image = PilImage.open(image)

            # Проверяем режим изображения
            if pil_image.mode in ["RGBA", "LA"] or (
                pil_image.mode == "P" and "transparency" in pil_image.info
            ):
                raise forms.ValidationError(
                    "Изображение содержит альфа-канал и не может быть загружено.Это не JPG"
                )
        return image
