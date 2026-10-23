def average(*numbers):
    total = 0
    for i in numbers:
        total += i
    try:
        avg = total / len(numbers)
    except ZeroDivisionError:
        avg = None
    return avg

print(average(2, 4, 9))
print(average())
values = [1, 2, 3]
print(average(*values))
