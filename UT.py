import unittest
import json
from app import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all_tasks(self):
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertIn('tasks', data)

    def test_create_task(self):
        new_task = {
            'title': 'Test Task',
            'description': 'This is a test task',
            'status': 'Not started',
            'priority': 'Low',
            'due_date': '2023-05-01'
        }
        response = self.app.post('/tasks', json=new_task)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertIn('task', data)
        task = data['task']
        self.assertIsNotNone(task['id'])
        self.assertEqual(task['title'], new_task['title'])
        self.assertEqual(task['description'], new_task['description'])
        self.assertEqual(task['status'], new_task['status'])
        self.assertEqual(task['priority'], new_task['priority'])
        self.assertEqual(task['due_date'], new_task['due_date'])

    def test_get_task_by_id(self):
        response = self.app.get('/tasks/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertIn('id', data)
        self.assertEqual(data['id'], 1)

    def test_update_task(self):
        updated_task = {
            'title': 'Updated Test Task',
            'description': 'This is an updated test task',
            'status': 'In progress',
            'priority': 'High',
            'due_date': '2023-05-02'
        }
        response = self.app.put('/tasks/1', json=updated_task)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertIn('id', data)
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['title'], updated_task['title'])
        self.assertEqual(data['description'], updated_task['description'])
        self.assertEqual(data['status'], updated_task['status'])
        self.assertEqual(data['priority'], updated_task['priority'])
        self.assertEqual(data['due_date'], updated_task['due_date'])

    def test_delete_task(self):
        response = self.app.delete('/tasks/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertIn('result', data)
        self.assertEqual(data['result'], True)

    def test_get_tasks_by_status(self):
        response = self.app.get('/tasks?status=Not started')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertIn('tasks', data)
        for task in data['tasks']:
            self.assertEqual(task['status'], 'Not started')

if __name__ == '__main__':
    unittest.main()