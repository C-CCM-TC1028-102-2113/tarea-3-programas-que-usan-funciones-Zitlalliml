
def main():
    #escribe tu código abajo de esta línea
    def main():
        b=float(input('Dame la base: '))
        h=float(input('Dame la altura: '))
        A= b*h

        volumen(A)
        return(A)

    def volumen (t):
        p=float(input('Dame la profundidad: '))
        vol= t * p

        print('El volumen del prisma es:' + str(vol))
    pass

if __name__=='__main__':
    main()
