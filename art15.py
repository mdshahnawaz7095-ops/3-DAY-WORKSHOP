n = int(input("Enter number: "))

count = 0

while n:
    count += n & 1
    n = n >> 1

print("Set bits =", count)