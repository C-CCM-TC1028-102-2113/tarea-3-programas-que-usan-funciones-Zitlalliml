
def main():
    #escribe tu código abajo de esta línea
    pa=int(input('Dame la cantidad de pliegos de papel albanene: '))
    pl=int(input('Dame la cantidad de plumones: '))
    pat= pa*12
    plt= pl*35
    cards(pat,plt)

def cards (a,b):
    if a <= b:
        max= a
    elif b <= a:
        max = b

    print('El número máximo de tarjetas que se pueden hacer es: ' + str(max))    
    return (max)
   
    pass

if __name__=='__main__':
    main()
