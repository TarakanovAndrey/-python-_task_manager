from django.test import TestCase
from . models import Status


class UserTestCase(TestCase):
    def setUp(self):
        Status.objects.create(name="Status1")

    def test_status_create(self):
        status = Status.objects.get(name='Status1')
        self.assertEqual(status.name, 'Status1')

    def test_user_update(self):
        status = Status.objects.get(name='Status1')
        status.status_name = 'Status2'
        self.assertEqual(status.status_name, 'Status2')

    def test_user_delete(self):
        status = Status.objects.get(name='Status1')
        status.delete()
        self.assertNotIn(status, Status.objects.all())
