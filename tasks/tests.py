from django.test import TestCase
from . models import Task
from django.contrib.auth.models import User
from statuses.models import Status


class TaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='user1')
        self.status = Status.objects.create(name='status1')
        Task.objects.create(name="Task1", status=self.status, author=self.user)

    def test_task_create(self):
        task = Task.objects.get(name='Task1')
        self.assertEqual(task.name, 'Task1')

    def test_label_update(self):
        task = Task.objects.get(name='Task1')
        task.name = 'Task2'
        self.assertEqual(task.name, 'Task2')

    def test_label_delete(self):
        task = Task.objects.get(name='Task1')
        task.delete()
        self.assertNotIn(task, Task.objects.all())
