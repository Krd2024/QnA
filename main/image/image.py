from django.shortcuts import render, redirect

from main.models import User, Image

from django.shortcuts import render

from ..forms import ImageForm

import os
import shutil


def delete_folder(folder_path):
    """Удалить текущую папку uuid перед созданием новой"""
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Папка '{folder_path}' успешно удалена.")
    else:
        print(f"Папка '{folder_path}' не существует.")


def image_upload_view(request):
    """Загрузка фото пользователя"""

    def save_image_url_user(img_obj):
        User.objects.filter(
            username=request.user.username,
        ).update(image_url=str(img_obj)[23:59])

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img_obj = Image.objects.filter(user_id=request.user)
            if img_obj is not None:
                img_obj.delete()

            image = form.save(commit=False)
            image.user = request.user
            image.save()

            img_obj = form.instance
            #
            print(form.cleaned_data["image"])
            #
            if form.cleaned_data["image"] is None:
                return render(request, "load_img.html", {"form": form})

            # Получить имя папки для удаления перед созданием новой (uuid)
            user_obj = User.objects.filter(username=request.user.username).first()
            dir_uuid = user_obj.image_url
            print(dir_uuid, "<<<<<< ---------- user_obj")

            if dir_uuid == "":
                save_image_url_user(img_obj.image)
                return redirect("user_profile", request.user.username)

            folder_path = f"static/profile/picture/{dir_uuid}"
            delete_folder(folder_path)

            save_image_url_user(img_obj.image)
            #
        return redirect("user_profile", request.user.username)
    else:
        form = ImageForm()
    return render(request, "load_img.html", {"form": form})
