import timeit

def fibona(x:int):
    i = 0
    m1 = 0
    m2 = 1
    while i <= x:
        f = m1 + m2
        m1 = m2
        m2 = f
        i +=1
    return f

if __name__=="__main__":
    i = int(input("Ingrese un número: "))
    fibo = fibona(i)
    fibon = timeit.default_timer()
    tiempo = timeit.default_timer() - fibon
    print("El número de fibonachi hasta el es que se ingreso es "+str(fibo))
    print("el tiempo que se demora es "+str(tiempo))