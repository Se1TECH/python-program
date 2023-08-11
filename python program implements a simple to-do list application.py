# python program implements a simple 
# to-do list application.

class Task:
    def __init__(self,description):
        self.description = description
        self.completed = False
    
class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self):
        description = input("Enter task Description: ")
        task = Task(description)
        self.tasks.append(task)
        print("Task Added Successfully")
    
    def complete_task(self):
        if not self.tasks:
            print("No Tasks Found")
        else:
            self.display_task()
            task_index = int(input("Enter The index for to list to make mark as read: "))
            if 0 <= task_index < len(self.tasks):
                self.tasks[task_index].completed = True
                print("Task marked as completed")
            else:
                print("Invalid task index")
    
    def display_task(self):
        if not self.tasks:
            print("No tasks found")
        else:
            print("\n\n----- Task List -----")
            for index,task in enumerate(self.tasks):
                status = "Completed " if task.completed else "Not Completed" 
                print(f"[{index}] {task.description} - {status}")

#create a todo list
todo_list = TodoList()

#menu loop
while True:
    print("\n\n----- Todo list Application -----")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("Enter Your Choice: ")
    if choice == "1":
        todo_list.add_task()
       
    elif choice == "2":
        todo_list.complete_task()
    
    elif choice == "3":
        todo_list.display_task()
    
    elif choice == "4":
        print("We are exiting")
        break
    
    else:
        print("Invalid choice, Try Again.")
    



