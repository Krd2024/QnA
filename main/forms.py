from django.forms import BaseModelForm, ModelForm
from .models import Question


# class QForm(BaseModelForm):
class QForm(ModelForm):

    class Meta:
        model = Question
        fields = "__all__"
