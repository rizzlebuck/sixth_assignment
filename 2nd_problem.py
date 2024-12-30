# Task 1
shopping_list = []
def add_to_shopping_list():
    print("Welcome to your Shopping List")
    while True:
        item = input("Enter the item(s) you wish to add then/or enter 'done' to exit:")
        if item == "done":
            print("Let me know if you'd like to add more items")
            break
        elif item not in shopping_list:
            shopping_list.append(item)
            print(f"{item} added to list")
        else:
            print("Item(s) is already in shopping list")

add_to_shopping_list()

# Task 2
shopping_list = []
def add_to_shopping_list():
    print("Welcome to your Shopping List")
    while True:
        item = input("Enter the item(s) you wish to add then/or enter 'done' to exit:")
        if item == "done":
            print("Let me know if you'd like to add more items")
            break
        elif item not in shopping_list:
            shopping_list.append(item)
            print(f"{item} added to list")
        else:
            print("Item(s) is already in shopping list")

def remove_from_shopping_list():
    print("Welcome to your Shopping List")
    while True:
        item = input("Enter the item you want to remove then/or enter 'done' to exit: ")
        if item == "done":
            print("Item(s) has been removed")
            break
        elif item in shopping_list:
            shopping_list.remove(item)
            print(shopping_list)
            print(f"{item} has been removed")
        else:
            print(f"{item} is not in your shopping list")


add_to_shopping_list()
remove_from_shopping_list()

# Task 3
shopping_list = []
def add_to_shopping_list():
    print("Welcome to your Shopping List")
    while True:
        item = input("Enter the item(s) you wish to add then/or enter 'done' to exit:")
        if item == "done":
            print("Let me know if you'd like to add more items")
            break
        elif item not in shopping_list:
            shopping_list.append(item)
            print(f"{item} added to list")
        else:
            print("Item(s) is already in shopping list")

def remove_from_shopping_list():
    print("Welcome to your Shopping List")
    while True:
        item = input("Enter the item you want to remove then/or enter 'done' to exit: ")
        if item == "done":
            print("Item(s) has been removed")
            break
        elif item in shopping_list:
            shopping_list.remove(item)
            print(shopping_list)
            print(f"{item} has been removed")
        else:
            print(f"{item} is not in your shopping list")

def view_shopping_list():
    if shopping_list:
        print(f"This is your current shopping list: {shopping_list}")
    else:
        print("Shopping List is empty")

add_to_shopping_list()
remove_from_shopping_list()
view_shopping_list()