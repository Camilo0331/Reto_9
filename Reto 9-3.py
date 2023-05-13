def potencia(b: int, p: int):
    if p == 1:
        return b
    elif p == 0:
        return 1
    else:
        return b * potencia(b, p - 1)

if __name__=="__main__":
    b = int(input("Ingrese la base: "))
    p = int(input("Ingrese el número al que va a ser elevado: "))
    poten = potencia(b,p)
    print(poten)