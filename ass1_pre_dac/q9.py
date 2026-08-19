n = int(input("Enter Number: "))

print("Given Number:", n)
print("Binary equivalent:", bin(n)[2:])
print("Octal equivalent:", oct(n)[2:])
print("Hexadecimal equivalent:", hex(n)[2:].upper())


def convert(n, base):
    digits = "0123456789ABCDEF"
    result = ""

    if n == 0:
        return "0"

    while n > 0:
        remainder = n % base
        result += digits[remainder]
        n //= base

    return result[::-1]


n = int(input("Enter Number: "))

print("Given Number:", n)
print("Binary equivalent:", convert(n, 2))
print("Octal equivalent:", convert(n, 8))
print("Hexadecimal equivalent:", convert(n, 16))