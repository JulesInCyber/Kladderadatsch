"""
better logic through functions.
functionality as shopping.py
"""

def parse_input(line: str) -> tuple[str, str | None]:
    """ splits command and item from user input"""
    parsed = line.split(maxsplit = 1)
    if len(parsed) == 1:
        parsed = (parsed[0], None)
    return parsed

def add_item(items: list[str], item: str) ->str:
    """ Add Item(s) to a list)"""
    items.append(item)
    msg = f"Added: {item}"
    return msg

def format_list(items: list[str]) -> str:
    item_list = []
    for i, item in enumerate(items, start=1):
        item_list.append(f"{i}. {item}")
    joined = ("\n").join(item_list)
    return joined

shopping_list = []
# Test-Cases
# print(add_item(shopping_list, "milk"))  # Success
# print(format_list(shopping_list))       # Success
# print(parse_input("add oat milk"))      # Success
print(parse_input("any"))
print(parse_input(""))
if __name__ == "__main__":
    pass
