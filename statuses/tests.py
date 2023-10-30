from django.test import TestCase
from . models import Status


class StatusTestCase(TestCase):
    def setUp(self):
        Status.objects.create(name="Status1")

    def test_status_create(self):
        status = Status.objects.get(name='Status1')
        self.assertEqual(status.name, 'Status1')

    def test_status_update(self):
        status = Status.objects.get(name='Status1')
        status.name = 'Status2'
        self.assertEqual(status.name, 'Status2')

    def test_status_delete(self):
        status = Status.objects.get(name='Status1')
        status.delete()
        self.assertNotIn(status, Status.objects.all())
