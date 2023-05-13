# Reto_9
## Punto 1

De los retos anteriores seleciones 3 funciones y escribalas en forma de lambdas.

Para este punto tome la funciones que hemos realizado a principio y utilice las funciones lambda.

```
n = int(input("Ingrese un número: "))
i = int(input("Ingrese un número: "))
sum = (lambda a, b: a+b)(n,i)
print("La suma de "+str(n)+" y "+str(i)+" es "+str(sum))
multi = (lambda a,b: a*b)(n,i)
print("La multiplicación de "+str(n)+" y "+str(i)+" es "+str(multi))
expo= (lambda a,b: a**b)(n,i)
print(str(n)+" elevado a "+str(i)+" es "+str(expo))

```

## Punto 2

De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).

```
def promedio(*args):
    sum = 0
    for i in args:
        sum += i
    prom = sum/len(args)
    return prom

def multi(*args):
    m = 1
    for i in args:
        m *= i
    return m

def factorial(args):
    fac = 1
    for i in range(1,args+1):
        fac *= i
    return fac



if __name__ == "__main__":
  a = int(input("Ingrese numero a: "))
  b = int(input("Ingrese numero b: "))
  c = int(input("Ingrese numero c: "))
  d = int(input("Ingrese numero d: "))
  e = int(input("Ingrese numero e: "))
  print("El promedio de los números ingresados es "+str(promedio(a,b,c,d,e)))
  print("La multiplicación de los 5 números ingresados es "+str(multi(a,b,c,d,e)))
  print("El factorial de A es "+ str(factorial(a)))

```

## Punto 3

Escriba una función recursiva para calcular la operación de la potencia.

```
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
```

## Punto 4

Utilice la siguiente plantilla de code para contar el tiempo:

```
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
```

### ¡No olvides dejar tu estrella!
