import sys
max_num = int(sys.argv[1])
for i in range(1, len(sys.argv)):
    num = int(sys.argv[i])
    if num > max_num:
        max_num = num
print(max_num)