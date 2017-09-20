def main(dat_media, dat_moda, dat_mediana):
    calculo_media(dat_media)
    calculo_moda(dat_moda)
    calculo_mediana(dat_mediana)

def calculo_media(arg):
    media = sum(arg)/len(arg)
    print('La media es: {}'.format(media))

def calculo_moda(arg):
    repeticiones = 0
    modas = []
    for i in arg:
        apariciones = arg.count(i)
        if apariciones > repeticiones:
            repeticiones = apariciones
    for i in arg:
        apariciones = arg.count(i)
        if apariciones == repeticiones and i not in modas:
            modas.append(i)
    print_modas(modas)

def calculo_mediana(arg):
    arg.sort()
    if len(arg) % 2 == 0:
        n = len(arg)
        mediana = ( arg[int((n/2)-1)] + arg[int(n/2)] ) / 2
    else:
        mediana = arg[int(len(arg)/2)]
    print('La mediana es: {}'.format(mediana))

def print_modas(modas):
    modas_char = ''
    for i in modas:
        modas_char += str(i) + ' '
    if len(modas)>1:
        print('Las modas son: {}'.format(modas_char))
    else:
        print('La moda es: {}'.format(modas_char))

if __name__ == '__main__':
    dat1=[1525, 257, 378, 9543, 7854, 152]
    dat2=[9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]
    dat3=[9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]
    main(dat1,dat2,dat3)
