def calculo_pendiente(x, y, n):
    p = []
    for i in range(n):
        p.append(x[i] * y[i])
    suma_p = sum(p)
    suma_y = sum(y)
    suma_x = sum(x)
    x_elevado2 = []
    for i in x:
        x_elevado2.append(i**2)
    suma_xi_elevado2 = sum(x_elevado2)
    sumax_elevado2 = sum(x)**2

    b = (((n*suma_p)-(suma_y*suma_x))/((n*suma_xi_elevado2)-sumax_elevado2))
    return b

def calculo_interseccion_de_la_linea(x,y,n,b):
    media_y = sum(y)/n
    media_x = sum(x)/n
    a = media_y-(b*media_x)
    return a

if __name__ == '__main__':
    t = 35
    x = [5, 15, 20, 25]
    y = [375, 487, 450, 500]
    n = len(x)
    b = calculo_pendiente(x, y, n)
    a = calculo_interseccion_de_la_linea(x,y,n,b)
    prediccion = a+b*t
    print('La pendiente es: {}'.format(b))
    print('El punto deinterseccion es: {}'.format(a))
    print('El precio predicho para la casa de {} metros cuadrados es: {:f}'.format(t,prediccion))
