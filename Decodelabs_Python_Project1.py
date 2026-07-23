task_list = []

def show_menu():
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")
    print("================================")

while True:
    show_menu()
    choice = input("Enter your choice (1-5) : ")

    if choice == "1":
        task = input("Enter a new task : ")
        task_list.append({"task" : task, "completed": False})
        print("✅ Task added successfully !")

    elif choice == "2":
        if len(task_list) == 0:
            print("No tasks available in your task list .")
        else:
            print("\n------ Your Tasks ------")
            for i , item in enumerate(task_list, start=1):
                status = "✔ Completed" if item["completed"] else "❌ Pending"
                print(f"{i}.{item["task"]} - {status}")

    elif choice == "3":
        if len(task_list) == 0:
            print("No tasks complete yet do it and then mark as completed .")
        else:
            for i, item in enumerate(task_list, start=1):
                print(f"{i}. {item["task"]}")
            try:
                task_no = int(input("Enter task number to mark as completed : "))
                if 1 <= task_no <= len(task_list):
                    task_list[task_no - 1]["completed"] = True
                    print("✅ Task marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number !")

    elif choice == "4":
        if len(task_list) == 0:
            print("No tasks to remove because of there is no any items in your task list !")
        else:
            for i, item in enumerate(task_list, start=1):
                print(f"{i}.{item["task"]}")
            try:
                task_no = int(input("Enter task number to remove : "))
                if 1 <= task_no <= len(task_list):
                    removed = task_list.pop(task_no - 1)
                    print(f"📢 Task '{removed["task"]}' removed successfully!")
                else:
                    print("Invalid task number .")
            except ValueError:
                print("Please enter a valid number from your task serial number !")

    elif choice == "5":
        print("Thank you for using my TO-DO List Application ! See you again....")
        break

    else:
        print("Invalid choice . Please enter a valid number between 1 and 5 !....")