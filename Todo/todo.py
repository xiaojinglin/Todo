options = ['Check todo', 'Add todo', 'Delete todo']
todo_list = []

def check_todo():
    if len(todo_list) == 0:
            print("You have nothing in your todo list")
    else:
        for todo_index, todo in enumerate(todo_list,1):
            print(f"{todo_index}.{todo}")


def add_todo():
    print("What do you want to add to the todo list?")
    enter = input()
    todo_list.append(enter)
    print("You just added one new thing to your todo list!")

def del_todo():
    del_success = True
    check_todo()
    enter = input("Enter the number of which you want to delete: ")
    length_todo = len(todo_list)
    if (not enter.isnumeric()) or (int(enter) not in range(1,length_todo + 1)):
        print("Invalid Input")
        del_success = False
    else :
        del_index = int(enter) - 1
        del todo_list[del_index]
        print("You just deleted one thing from your todo list!")
    return del_success


while True:
    for option_index, option in enumerate(options,1):
        print(f"{option_index}.{option}")
    enter = input("Enter a number between 1 to 3 to choose an option: ")
    if (not enter.isnumeric()) or (int(enter) not in range(1,4)):
        print("Invalid Input")
        continue
    enter = int(enter)
    if enter == 1:
        check_todo()
    elif enter == 2:
        add_todo()
    else:
        del_success = del_todo()
        if not del_success:
            print("Invalid Input")
            continue
    enter = input("Enter 'c' to continue, any other to quit: ")
    if enter == 'c':
        continue
    else:
        exit()