text = input("Enter a string: ")

count = {}

for ch in text.upper():
    if 'A' <= ch <= 'Z':
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

for ch in count:
    print(ch, ":", count[ch])