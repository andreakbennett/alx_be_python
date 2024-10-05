#!/usr/bin/env python3
shopping_list = []
def display_menu():
    print(f"Shopping List Manager")  
    print(f"1. Add item") 
    print(f"2. Remove item")
    print(f"3. View list")
    print(f"4. Exit")

def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to the shopping list.")

def remove_item():
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' is not in the shopping list.")

def view_list():
    if shopping_list:
        print("\nShopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("The shopping list is currently empty.")

while True:
    display_menu()
    
    choice = input("Choose an option (1-4): ")
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_list()
    elif choice == "4":
        print("Exiting the shopping list manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")
