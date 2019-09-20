a = int(input("Input first equation:"))
b = int(input("Input second equation:"))
c = int(input("Input third equation:"))

delta = b ** 2 - 4 * a * c

x1 = (-b - delta ** 0.5) / (2*a)

x2 = (-b + delta ** 0.5) / (2*a)

print("First equation : {}".format(x1))
print("Second equation : {}".format(x2))