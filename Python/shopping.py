def show_list(any_list):
    for i in range(len(shopping_list)):
        print(f"{i+1}. {shopping_list[i]}")

shopping_list = []

while True:
    user_input = input("> ").lower()
    args = [word for word in user_input.split()]
    list_command = args[0]
    if list_command == "add":
        shopping_list.append(args[1])
        print(f"Added: {args[1]}")
    elif list_command == "remove":
        if args[1] in shopping_list:
            shopping_list.remove(args[1])
        else:
            print(f"Not on the list: {args[1]}")
    elif list_command == "list":
        show_list(shopping_list)
    elif list_command == "quit":
        print("Bye!")
        break
    else:
        print("Unknown command. Use: add, remove, list, quit")
