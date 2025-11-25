a = 1
b = 1

print(a)
print(b)

count = 2
while count < 60:
    c = a + b
    print(f"{a} + {b} = {c}")
    a = b
    b = c
    count += 1

