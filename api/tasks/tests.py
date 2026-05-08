from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            is_completed=False
        )

    #test GET all tasks
    def test_view_tasks(self):
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #test GET one task   
    def test_fetch_task(self):
        response = self.client.get(f"/api/tasks/{self.task.id}") 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #test POST task
    def test_create_task(self):
        data = {
            "title": "New Task",
            "description": "Task Description",
            "is_completed": False
        }
        response = self.client.post("/api/tasks/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #test PUT a task
    def test_update_task(self):
        data = {
            "title": "Updated Task",
            "description": "Updated Description",
            "is_completed": True
        }
        response = self.client.put(f"/api/tasks/{self.task.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #test DELETE task
    def  test_delete_task(self):
        response = self.client.delete(f"/api/tasks/{self.task.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)   