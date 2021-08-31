
def main():
    #escribe tu código abajo de esta línea
    año=int(input())
    if (año % 4) == 0 and (año % 100) != 0 or (año% 400) == 0:
        bin= True
    else:
        bin= False
  
    print (str(bin))
    pass

if __name__=='__main__':
    main()
