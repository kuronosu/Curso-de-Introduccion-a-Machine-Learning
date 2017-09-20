def main():
    fibonacci=[0,1]
    x, y = fibonacci[0], fibonacci[1]
    num = int(input("Hasta la posición: "))
    if num == 0:
        print('Posición:\t{}' .format(0))
        print('Secuencia:\t{}'.format(0))
        return
    for n in range(num-1):
        fibonacci.append(x+y)
        a = x + y
        x = y
        y = a
    print('Posición:\t{}' .format(list(range(num+1))))
    print('Secuencia:\t{}'.format(fibonacci))

if __name__ == '__main__':
    main()
