def g(pesos, a, b):
    salida = (pesos[0] + pesos[1]*a + pesos[2]*b)
    if salida < 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    a = [0,0,1,1]
    b = [0,1,0,1]
    pesos_or = [-10,20,20]
    pesos_and = [-30,20,20]
    salida_or = []
    salida_and = []
    for i in range(len(a)):
        salida_or.append(g(pesos_or, a[i], b[i]))
        salida_and.append(g(pesos_and, a[i], b[i]))

    print('El output de la conpuerta logica or es: {}'.format(salida_or))
    print('El output de la conpuerta logica and es: {}'.format(salida_and))
