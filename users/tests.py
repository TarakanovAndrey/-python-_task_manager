from django.test import TestCase, Client
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(
            first_name='User',
            last_name='Userovich',
            username='User1',
            password='111',

        )

    def test_user_create(self):
        user = User.objects.get(username='User1')
        self.assertEqual(user.first_name, 'User')

    def test_user_login(self):
        c = Client()
        response = c.post('/login/', {'username': 'User', 'password': 111})
        self.assertEqual(response.status_code, 200)

    def test_user_logout(self):
        c = Client()
        response = c.post('/logout/', {'username': 'User', 'password': 111})
        self.assertEqual(response.status_code, 302)

    def test_user_update(self):
        user = User.objects.get(username='User1')
        user.first_name = 'UserUser'
        self.assertEqual(user.first_name, 'UserUser')

    def test_user_delete(self):
        user = User.objects.get(username='User1')
        user.delete()
        self.assertNotIn(user, User.objects.all())
