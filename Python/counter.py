def increment(number: int) -> int:
    number += 1
    return number


# Test-Case
counter = 0
counter = increment(counter)
counter = increment(counter)
print(counter) # Expected: 2
