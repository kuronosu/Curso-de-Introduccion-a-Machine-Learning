fibonacci=[0,1]
x, y = fibonacci[0], fibonacci[1]
num = int(input("Numero de elementos:"))
for n in range(num-1):
    fibonacci.append(x+y)
    a = x + y
    x = y
    y = a
print(fibonacci)
