def menu():
    print("What do you want to do:")
    print("A:Add a task")
    print("D:Delete a task")
    print("S:See task list")
    print("X:Exit")
    option = input()
    
    if option == 'A':
        add_task()
    elif option == 'D':
        delete_task()
    elif option == 'S':
        see_list()
    elif option == 'X':
        exit
    else:
        print('Not a valid option.')
        menu()
            

def add_task():
    task_input = input('Enter task: ')
    task_list.append(task_input)
    print(f'{task_input} added to your list.')
    menu()

def delete_task():
    if len(task_list) < 1:
        print('Your task list is empty.')
    else:
        task_input = input('Enter task: ')
        if task_input in task_list:
            task_list.remove(task_input)
            print("Task deleted from your list")
            menu()
        else:
            print("Task does not exist.")
            delete_task()

def see_list():
    if len(task_list) < 1:
        print('Your task list is empty.')
        menu()
    else:
        for i in task_list:
            print(f'{task_list.index(i)+1}: {i}')
        menu()
    

task_list = []

menu()