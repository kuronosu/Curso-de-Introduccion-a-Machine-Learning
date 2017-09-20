import math

def cal_varianza(arg):
    #paso 1
    suma = sum(arg)
    #paso 2
    media = suma/len(arg)
    #paso 3
    paso3 = []
    for i in arg:
        paso3.append(i - media)
    #paso 4
    paso4 = []
    for i in paso3:
        paso4.append(pow(i,2))
    #paso 5
    varianza = (sum(paso4)/len(paso4))
    return varianza

def cal_desviacion_estandar(arg):
    #paso6
    return math.sqrt(arg)

if __name__ == '__main__':
    dat=[13, 14, 15, 15, 15, 16, 17, 18, 20]
    varianza = cal_varianza(dat)
    desviacion_estandar = cal_desviacion_estandar(varianza)
    print('La varianza es: {}, y la desviación estándar es: {}'.format(varianza, desviacion_estandar))
