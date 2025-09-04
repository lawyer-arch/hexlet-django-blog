from django.test import TestCase
from django.urls import reverse


class UsersTest(TestCase):
    def test_users_list(self):
        # Первый запрос - получаем редирект
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)  # Проверяем, что происходит редирект
        