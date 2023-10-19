from django.test import TestCase
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(
            username='User1',
            password='111',
            first_name='User',
            last_name='Userovich'
        )

    def test_user_create(self):
        user = User.objects.get(username='User1')
        self.assertEqual(user.first_name, 'User')
