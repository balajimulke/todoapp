from django.test import TestCase
from .models import TodoItem

class TodoItemModelTest(TestCase):

    def setUp(self):
        # Create a sample task for testing
        self.task = TodoItem.objects.create(title="Test Task")

    def test_task_creation(self):
        """Test if the task is created successfully"""
        self.assertEqual(self.task.title, "Test Task")
        self.assertIsNotNone(self.task.timestamp)

    def test_task_string_representation(self):
        """Test the string representation of the task"""
        self.assertEqual(str(self.task), "Test Task")

from django.urls import reverse

class TodoListViewTest(TestCase):

    def setUp(self):
        # Create some sample tasks
        TodoItem.objects.create(title="Task 1")
        TodoItem.objects.create(title="Task 2")

    def test_todo_list_view_status_code(self):
        """Test if the todo_list view returns a 200 status code"""
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)

    def test_todo_list_view_content(self):
        """Test if the todo_list view displays tasks"""
        response = self.client.get(reverse('todo_list'))
        self.assertContains(response, "Task 1")
        self.assertContains(response, "Task 2")

class TodoCreateViewTest(TestCase):

    def test_todo_create_view_status_code(self):
        """Test if the todo_create view returns a 200 status code"""
        response = self.client.get(reverse('todo_create'))
        self.assertEqual(response.status_code, 200)

    def test_todo_create_view_form_submission(self):
        """Test if the form submission creates a new task"""
        response = self.client.post(reverse('todo_create'), {'title': 'New Task'})
        self.assertEqual(TodoItem.objects.count(), 1)
        self.assertEqual(TodoItem.objects.first().title, 'New Task')

#writing integration tests below
class TodoIntegrationTest(TestCase):

    def test_create_and_display_task(self):
        """Test the entire flow of creating and displaying a task"""
        # Create a new task
        self.client.post(reverse('todo_create'), {'title': 'Integration Task'})
        
        # Check if the task appears in the list view
        response = self.client.get(reverse('todo_list'))
        self.assertContains(response, 'Integration Task')

