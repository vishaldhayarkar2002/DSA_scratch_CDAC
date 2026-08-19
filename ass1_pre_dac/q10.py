n = int(input("Enter number of students (max 10): "))

names = []

for i in range(n):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

names.sort()

print("Sorted names:")
for name in names:
    print(name)