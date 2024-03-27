#Task 1: Write a function that lets the user add items to a list.

shopping_list = []

def add_to_shopping_list():
    global shopping_list
    while True:
        item = input("Type shopping list item or type 'done': ")
        if item.lower() == "done":
            break
        else:
            shopping_list.append(item)

add_to_shopping_list()

#Task 2: Include a feature to remove items from the list.

print(shopping_list)

def remove_item(item):
    global shopping_list
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed {item}! Here is the updated list:\n{shopping_list}")
    else:
        print(f"\"{item}\" is not in the list. Check again!")
        print(shopping_list)

while True:
    remove = input("Type an item to remove from the list or type done: ")
    if remove.lower() == "done":
        break
    else:
        remove_item(remove)

#Task 3: Add a function that prints out the entire list in a formatted way.

print("Here is your final formatted shopping list!:")
item_counter = 1
for item in shopping_list:
    print(f"{item_counter}. {item}")
    item_counter += 1