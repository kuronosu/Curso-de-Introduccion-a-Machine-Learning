import sys


def main():
    fibonacci=[0,1]
    x, y = fibonacci[0], fibonacci[1]
    num = int(input("Hasta la posición: "))
    if num < 0:
        return False, False
    elif num == 0:
        print('Posición:\t{}' .format(0))
        print('Secuencia:\t{}'.format(0))
        return
    for n in range(num-1):
        fibonacci.append(x+y)
        a = x + y
        x = y
        y = a
    ps = list(range(num+1))
    return ps, fibonacci
    

if __name__ == '__main__':
    position, fibonacci = main()
    if not position:
        print("Ingreso una Posición negativa")
        sys.exit(0)
    print("\t {0} \t {1}".format('posición','fibonacci'))
    for i in position:
        print("\t {0} \t\t {1}".format(position[i],fibonacci[i]))
