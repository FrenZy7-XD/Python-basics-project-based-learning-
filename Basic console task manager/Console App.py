#making a Console App/ Task organiser for the first time

tasks= [] #creating a empty list

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice=input("choice -> (1/2/3/4)")

    if choice=="1":
        tasks.append(input("add your task here ->"))

    elif choice=="2":
        print(tasks)
    elif choice=="3":
        tasks.remove(input("task to be deleted ->"))

    elif choice=="4":
        break

