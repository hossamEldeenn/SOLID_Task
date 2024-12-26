from abc import ABC,abstractmethod

class ITaskManagement(ABC):
    @abstractmethod
    def add_task(self, task):
        pass
    
    @abstractmethod
    def update_task_status(self, task_id, status):
        pass


class INotification(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass



class Task:
    def __init__(self, id, title, description, priority, status="Pending"):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status


class UrgentTask(Task):
    def __init__(self, id, title, description):
        super().__init__(id, title, description, priority="Urgent")


class Notification(INotification):
    def send_notification(self, message):
        print(f"Notification: {message}")


class TaskManager(ITaskManagement):
    def __init__(self, notifier: INotification):
        self.tasks = []
        self.notifier = notifier

    def add_task(self, task : Task):
        self.tasks.append(task)
        self.notifier.send_notification(f"Task '{task.title}' has been added.")

    def update_task_status(self, task_id, status):
        for task in self.tasks:
            if task.id == task_id:
                task.status = status
                self.notifier.send_notification(f"Task '{task.title}' status updated to '{status}'.")
                if status == "Done":
                    self.tasks.remove(task)
                break


    def list_tasks(self):
        return self.tasks
    
    def display_tasks(self):
        tasks_title = [task.title for task in self.tasks]
        print(f"Tasks in Task Manager now is : {tasks_title}")



message_notifier = Notification()
manager = TaskManager(message_notifier)

task1 = Task(1, "Study Python", "Revise OOP concepts", "Normal")
manager.add_task(task1)

task2 = UrgentTask(2, "Submit Assignment", "Complete the SOLID task")
manager.add_task(task2)

task3 = Task(3, "Study Data structure", "Revise Linked List", "Low")
manager.add_task(task3)
print('-'*20)

manager.update_task_status(1, "In Progress")
manager.update_task_status(1, "Done")
manager.update_task_status(2, "In Progress")
print('-'*20)

for task in manager.list_tasks():
   print(f"Task: {task.title}, Status: {task.status}")
   
manager.display_tasks()





    
    
            

