def average(*numbers):
    avg = 0
    for i in numbers:
        avg += i
    try:
        avg = avg / len(numbers)
    except:
        avg = None
    return avg

print(average(2, 4, 9))
print(average())
values = [1, 2, 3]
print(average(*values))
