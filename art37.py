x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > 0 and y > 0:
    print("First quadrant")
elif x < 0 and y > 0:
    print("Second quadrant")
elif x < 0 and y < 0:
    print("Third quadrant")
elif x > 0 and y < 0:
    print("Fourth quadrant")
else:
    print("Point lies on an axis")