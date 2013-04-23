import unittest
from tasks import *

class TaskListTests(unittest.TestCase):

    def test_can_add_task_to_list(self):
        # arrange
        task = Task()
        task_list = TaskList()
        # act
        task_list.add(task)
        # assert
        self.assertEquals(len(task_list), 1)
        self.assertEquals(task_list.get_task(0), task)

    def test_add_top_priority_adds_the_item_somewhere(self):
        task = Task()
        task_list = TaskList()
        task_list.add_top_priority(task)
        self.assertEquals(len(task_list), 1)

    def test_get_top_priority_after_adding_one(self):
        top_priority_task_in = Task()
        task2                = Task()
        task3                = Task()
        task_list            = TaskList()
        task_list.add(task2)
        task_list.add_top_priority(top_priority_task_in)
        task_list.add(task3)
        top_priority_task_out = task_list.get_top_priority()
        self.assertEquals(top_priority_task, top_priority_task_in)

    def test_an_empty_list_has_no_tasks(self):
        #arrange
        task_list = TaskList()
        self.assertEquals(len(task_list), 0)

    def test_add_two_tasks_to_the_list(self):
        #arrange
        task_list = TaskList()
        task1 = Task()
        task2 = Task()
        self.assertTrue(task1 != task2)
        task_list.add(task1)
        task_list.add(task2)
        self.assertEquals(task_list.get_task(1), task2)

    def test_get_the_list_of_tasks(self):
        task1 = Task("Buy Groceries", "ToDo")
        task2 = Task("Pay Rent", "InProgress")
        task3 = Task("Finish Code", "Done")
        task_list = TaskList()
        task_list.add(task1)
        task_list.add(task2)
        task_list.add(task3)

    def test_save(self):
	test_get_the_list_of_tasks()
        task.save()


class TaskTests(unittest.TestCase):
    def test_descrption_and_state(self):
        task=Task("Descripion","ToDo")
        self.assertEquals(task.status, "ToDo")
    

if __name__ == "__main__":
    unittest.main()
