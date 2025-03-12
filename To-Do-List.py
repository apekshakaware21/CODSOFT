import os

def display_menu():
    print("\nTo-Do List App")
    print("1. View To-Do List")
    print("2. Add To-Do Item")
    print("3. Remove To-Do Item")
    print("4. Exit")

def view_todo_list(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")

def add_todo_item(todo_list):
    item = input("\nEnter the to-do item: ")
    todo_list.append(item)
    print(f"'{item}' has been added to your to-do list.")

def remove_todo_item(todo_list):
    view_todo_list(todo_list)
    if todo_list:
        try:
            item_index = int(input("\nEnter the number of the item to remove: ")) - 1
            if 0 <= item_index < len(todo_list):
                removed_item = todo_list.pop(item_index)
                print(f"'{removed_item}' has been removed from your to-do list.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_todo_item(todo_list)
        elif choice == '3':
            remove_todo_item(todo_list)
        elif choice == '4':
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()