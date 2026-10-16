word = "banana"
letters = [l for l in word]

counts = {}

for letter in letters:
    counts[letter] = counts.get(letter, 0) + 1

print(counts)
