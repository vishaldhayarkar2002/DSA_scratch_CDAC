names = ["apple", "banana", "apple", "mango", "banana", "apple"]

seen = set()
duplicates = set()

for name in names:
    if name in seen:
        duplicates.add(name)
    else:
        seen.add(name)

print("Duplicate strings:")

for name in duplicates:
    print(name)