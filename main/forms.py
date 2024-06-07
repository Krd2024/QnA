from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Image, Teg
from PIL import Image as PilImage

from .models import Question, User


# class ProfileEditForm(UserCreationForm):
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "profession"]


class QForm(ModelForm):
    # teg = forms.ModelChoiceField(
    #     queryset=Teg.objects.all(), required=True, label="Выбор тега"
    # )

    class Meta:
        model = Question
        exclude = []
        fields = (
            "autor",
            "tegs",
            "title",
            "text",
        )
        # fields = "__all__"
        widgets = {
            "id": forms.HiddenInput(),
            "autor": forms.HiddenInput(),
        }


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
        fields = ("image",)

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
