from django.test import TestCase
from . models import Label


class LabelTestCase(TestCase):
    def setUp(self):
        Label.objects.create(name="Label1")

    def test_label_create(self):
        label = Label.objects.get(name='Label1')
        self.assertEqual(label.name, 'Label1')

    def test_label_update(self):
        label = Label.objects.get(name='Label1')
        label.name = 'Label2'
        self.assertEqual(label.name, 'Label2')

    def test_label_delete(self):
        label = Label.objects.get(name='Label1')
        label.delete()
        self.assertNotIn(label, Label.objects.all())
