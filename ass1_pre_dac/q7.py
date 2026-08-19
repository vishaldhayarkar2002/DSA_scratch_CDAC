start = int(input("Enter first number: "))
end = int(input("Enter second number: "))

for num in range(start, end + 1):
    print("Table of", num)

    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

    print()