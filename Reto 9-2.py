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

