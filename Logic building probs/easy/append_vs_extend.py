# 8. append() vs extend()
a = [1,2]

a.append([3,4])

print(a)

Output

[1, 2, [3, 4]]

Now,

a = [1,2]

a.extend([3,4])

print(a)

Output

[1,2,3,4]