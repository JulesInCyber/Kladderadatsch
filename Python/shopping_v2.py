"""
better logic through functions.
functionality as shopping.py
"""

def parse_input(line: str) -> tuple[str, str | None]:
    """ splits command and item from user input"""
    parsed = line.split(maxsplit = 1)
    if len(parsed) == 1:
        parsed = (parsed[0], None)
    elif len(parsed) == 0:
        parsed = ("",None)
    return parsed

def add_item(items: list[str], item: str) -> str:
    """ Add Item(s) to a list)"""
    items.append(item)
    msg = f"Added: {item}"
    return msg

def remove_item(items: list[str], item: str) -> str:
    """remove Item from list and display a message"""
    items.remove(item)
    msg = f"Removed: {item}"
    return msg

def format_list(items: list[str]) -> str:
    item_list = []
    for i, item in enumerate(items, start=1):
        item_list.append(f"{i}. {item}")
    joined = ("\n").join(item_list)
    return joined

# shopping_list = []
# Test-Cases
# print(add_item(shopping_list, "milk"))  # Success
# print(format_list(shopping_list))       # Success
# print(parse_input("add oat milk"))      # Success
# print(parse_input("any"))               # Success
# print(parse_input(""))                  # Success

if __name__ == "__main__":
    shopping_list = []
    while True:
        prompt_user = input("> ")
        command, item = parse_input(prompt_user)

        if command == "add":
            if item == None:
                print("No item specified")
            else:
                added_item = add_item(shopping_list, item)
                print(added_item)

        elif command == "remove":
            if item == None:
                print("No item specified")
            else:
                removed_item = remove_item(shopping_list, item)
                print(removed_item)

        elif command == "list":
            joined_list = format_list(shopping_list)
            if len(joined_list) == 0:
                print("Nothing on list")
            else:   
                print(joined_list)

        elif command == "quit":
            print("Bye")
            break

