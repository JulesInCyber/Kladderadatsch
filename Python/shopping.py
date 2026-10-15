def show_list(any_list):
    for i, item in enumerate(any_list):
        print(i+1, item)

shopping_list = []

while True:
    user_input = input("> ").lower().split(maxsplit = 1)
    try:
        list_command = user_input[0]
        if list_command == "add":
            if len(user_input) < 2:
                print("No Item Specified")
            else:
                shopping_list.append(user_input[1])
                print(f"Added: {user_input[1]}")

        elif list_command == "remove":
            if len(user_input) < 2:
                print("No Item Specified")
            else:
                if user_input[1] in shopping_list:
                    shopping_list.remove(user_input[1])
                    print(f"Removed: {user_input[1]}")
                else:
                    print(f"Not on the list: {user_input[1]}")

        elif list_command == "list":
            show_list(shopping_list)

        elif list_command == "quit":
            print("Bye!")
            break

        else:
            print("Unknown command. Use: add, remove, list, quit")
    except IndexError:
        print("Input cannot be empty!")
