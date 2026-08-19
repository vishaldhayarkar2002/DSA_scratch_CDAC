text = input("Enter a string: ")

reverse = ""

for i in range(len(text) - 1, -1, -1):
    reverse = reverse + text[i]

print("Reversed string:", reverse)

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print(reverse)
# using two pointer approach
text = list(input("Enter a string: "))

left = 0
right = len(text) - 1

while left < right:
    text[left], text[right] = text[right], text[left]

    left += 1
    right -= 1

print("".join(text))