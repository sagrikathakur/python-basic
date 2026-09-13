import os
import unittest
from task_manager.models import Task
from task_manager.storage import StorageManager


class TestTaskModel(unittest.TestCase):
    def test_task_creation(self):
        task = Task(1, "Study Python", "Read chapter on modules", priority="High")
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.title, "Study Python")
        self.assertEqual(task.status, "Pending")
        self.assertEqual(task.priority, "High")

    def test_task_serialization(self):
        task = Task(2, "Buy groceries", priority="Medium")
        data = task.to_dict()
        self.assertEqual(data["id"], 2)
        self.assertEqual(data["title"], "Buy groceries")

        reconstructed = Task.from_dict(data)
        self.assertEqual(reconstructed.task_id, 2)
        self.assertEqual(reconstructed.title, "Buy groceries")

    def test_task_status_toggle(self):
        task = Task(3, "Clean desk")
        self.assertEqual(task.status, "Pending")
        task.mark_completed()
        self.assertEqual(task.status, "Completed")
        task.mark_pending()
        self.assertEqual(task.status, "Pending")


class TestStorageManager(unittest.TestCase):
    TEST_FILE = "test_tasks.json"

    def setUp(self):
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)
        self.storage = StorageManager(self.TEST_FILE)

    def tearDown(self):
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_add_and_get_task(self):
        task = self.storage.add_task("Write code", "Create unit tests", priority="High")
        self.assertEqual(task.task_id, 1)
        
        retrieved = self.storage.get_task(1)
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.title, "Write code")

    def test_toggle_completion(self):
        task = self.storage.add_task("Review PR")
        self.assertEqual(task.status, "Pending")
        
        updated = self.storage.toggle_task_completion(1)
        self.assertIsNotNone(updated)
        self.assertEqual(updated.status, "Completed")

    def test_list_and_filter_tasks(self):
        self.storage.add_task("Task 1", priority="Low")
        t2 = self.storage.add_task("Task 2", priority="High")
        self.storage.toggle_task_completion(t2.task_id)

        all_tasks = self.storage.list_tasks()
        self.assertEqual(len(all_tasks), 2)

        completed_tasks = self.storage.list_tasks(status_filter="Completed")
        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(completed_tasks[0].task_id, t2.task_id)

        high_priority = self.storage.list_tasks(priority_filter="High")
        self.assertEqual(len(high_priority), 1)

    def test_delete_task(self):
        task = self.storage.add_task("Temporary Task")
        self.assertTrue(self.storage.delete_task(task.task_id))
        self.assertIsNone(self.storage.get_task(task.task_id))
        self.assertFalse(self.storage.delete_task(999))


if __name__ == "__main__":
    unittest.main()
