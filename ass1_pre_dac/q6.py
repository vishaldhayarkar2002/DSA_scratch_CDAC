r1 = int(input("Rows of first matrix: "))
c1 = int(input("Columns of first matrix: "))

r2 = int(input("Rows of second matrix: "))
c2 = int(input("Columns of second matrix: "))

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    A = []
    B = []

    print("Enter first matrix:")
    for i in range(r1):
        A.append(list(map(int, input().split())))

    print("Enter second matrix:")
    for i in range(r2):
        B.append(list(map(int, input().split())))

    result = [[0] * c2 for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    print("Result:")
    for row in result:
        print(*row)