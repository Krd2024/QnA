from django.test import TestCase, Client
from django.urls import reverse, resolve

from main.views.user import user_profile


# class Test(TestCase):

#     def test_1(self):
#         print("BASIC TEST:")

#         x = reverse("user_profile", kwargs={"username": "den"})
#         f = resolve(x).func

#         # print(f)
#         # print(user_profile)

#         assert f == user_profile

#         print()

#     def test_2(self):
#         client = Client()
#         res = client.get("/")
#         self.assertEqual(res.status_code, 200)

#     # def test_3(self):
#     #     client = Client()

#     #     self.assertEqual(client.get("/q/create").status_code, 301)

#     def test_4(self):
#         client = Client()
#         client.login(username="Den", password="1")
#         self.assertEqual(client.get("/q/create").status_code, 200)

from django.test import TestCase, Client


# from django.contrib.auth.models import User
from main.models import User


class MyTests(TestCase):
    def setUp(self):
        # Создаем пользователя для тестов
        self.user = User.objects.create_user(username="Denn", password="1")
        self.client = Client()
        print(self.user)

    def test_login(self):
        # Выполняем вход
        login = self.client.login(username="Denn", password="1")
        self.assertTrue(login)  # Проверяем, что вход выполнен успешно
        print(login, "<< ---- login ----")

    def test_some_view(self):
        # Выполняем вход перед доступом к защищенному представлению
        in_ = self.client.login(username="Denn", password="1")
        print(in_, "<< ------- in_")
        response = self.client.get("/q/create")
        self.assertEqual(response.status_code, 200)  # Проверяем успешный ответ


# Create your tests here.
