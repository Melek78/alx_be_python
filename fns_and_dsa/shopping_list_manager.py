def display_menu():
    print("shopping list manager")
    print("1. add item")
    print("2. remove item")
    print("3. list items")
    print("4. exit")
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = (input("choose from 1 - 4: "))
        if choice == "1":
            item = input("enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list")
        elif choice == "2":
            item = input("enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list")
            else:
                print(f"{item} not found in shopping list")
        elif choice == "3":
            print(shopping_list)
        elif choice == "4":
            break
        else:
            print("invalid input, enter from 1 - 4")

main()