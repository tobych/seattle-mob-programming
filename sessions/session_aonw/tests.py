import unittest

class Task:
    
    def __init__(self, description=None, status=None):
        self.description = description
        self.status = status
    

class TaskList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def __len__(self):
        return len(self.tasks)

    def get_task(self, index):
        return self.tasks[index]

    def get_current_tasks(self):
        

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


3) Done\tFinish Code"""3) Done\tFinish Code"""3) Done\tFinish Code"""3) Done\tFinish Code"""3) Done\tFinish Code"""

    pass



class TaskList:
    pass
    def add(task):
        pass
class SomethingTestCase(unittest.TestCase):
2) InProgress\tPay Rent

3) Done\tFinish Code"""


        self.assertEquals(task_list.get_current_tasks(), expected_string)


    def test_we_can_give_a_task_a_description(self):
        #arrange
        task = Task("Description")
        #act
        #assert
        self.assertEquals(task.description, "Description")

class TaskTests(unittest.TestCase):
    
    def test_descrption_and_state(self):
        task=Task("Descripion","ToDo")
        self.assertEquals(task.status, "ToDo")

    

if __name__ == "__main__":
    unittest.main()
