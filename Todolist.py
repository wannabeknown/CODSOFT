class Todolist:
    def __init__(self):
        self.tasks = []

    def ADDTASK(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' You Have Mentioned Has Been Added To The List ")
    def RMTASK(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' You Have Mentioned Has Been Removed From The List")
        else:
            print(f"Task '{task}' You Have Mentioned Has Been Removed From The List")

    def SHOW(self):
        if self.tasks:
            print("To-Do List")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("Your To-do List is Empty Please Enter A Task First")

def display_menu():
    print("\nOptions:")
    print("1. Add A Task To Add")
    print("2. Remove Task From The List")
    print("3. Show All The Task ")
    print("4. Out")

def main():
    todo_list = Todolist()

    while True:
        display_menu()
        choice = input(f"Select A Option From The Above")

        if choice == "1":
            task = input(f"Enter A Task You Have To Add")
            todo_list.ADDTASK(task)
        elif choice == "2":
            task = input(f"Enter The Task Which You Have To Remove")
            todo_list.RMTASK(task)
        elif choice == "3":
            todo_list.SHOW()
        elif choice == "4":
            print("Closing The List")
            break
        else:
            print("The Option You Have Entered Is Wrong Please Select A Correct Option")

if __name__ == "__main__":
    main()