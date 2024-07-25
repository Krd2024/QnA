# from django.db import models
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     phone_number = models.CharField(max_length=12)


# class Review(models.Model):
#     text = models.TextField(verbose_name="Текст отзыва")
#     rating = models.IntegerField(
#         verbose_name="Оценка",
#         choices=[
#             (1, "1"),
#             (2, "2"),
#             (3, "3"),
#             (4, "4"),
#             (5, "5"),
#         ],
#     )
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
#     updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
#     user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Продукт")

#     def __str__(self):
#         return self.text

# =================================================================
#                forms

# from models import Review, User
# from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from django import forms


# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ("text", "rating")


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField(required=False)

#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]

#     def save(self, commit=True):
#         user = super(UserRegisterForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         user.is_active = False  # Делает аккаунт неактивным до подтверждения email
#         if commit:
#             user.save()
#         return user
# =================================================================
#   представление

#     def create_review(request, product_id):
# if request.method == "POST":
#     form = ReviewForm(request.POST)
#     if form.is_valid():
#         review = form.save(commit=False)
#         review.product_id = product_id
#         review.save()
#         return redirect("product_detail", product_id=product_id)
# else:
#     form = ReviewForm()
# return render(request, "reviews/create_review.html", {"form": form})
