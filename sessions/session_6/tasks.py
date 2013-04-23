import json

class Task:

    def __init__(self, description=None, status=None):
        self.description = description
        self.status = status


class TaskList:

    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def add_top_priority(self, task):
        self.tasks.insert(0, task)

    def get_top_priority(self):
        return self.tasks[0]

    def __len__(self):
        return len(self.tasks)

    def get_task(self, index):
        return self.tasks[index]

    def get_current_tasks(self):
        pass

    def save(self):
        s = json.dumps(self.tasks)
        # write s to file
        f = file('tasks.json','w')
        f.write(s)
        f.close()

    def load(self):
        f = file('tasks.json','r')
        # read  s from file
	s = f.read()
	f.close()
        self.tasks = json.loads(s)
	#
	print self.tasks

if __name__ == "__main__":
    pass
