#Eleccion de ejercicio
a=int(input("Seleccione un ejercicio entre 1, 2, 3, 4, 7, 8, 9, 10, 11 o 12: "))

if a==1:
    #Ejercicio1
    num=float(input("Ingrese un número o -1 para terminar: "))
    if num !=-1:
        primero = num
        while num!=-1:
            final=num
            num=float(input("Ingrese un número o -1 para terminar: "))
        print("El primer número es", primero)
        print("El último número es", final)
    else:
        print("Error, ingrese un valor válido.")

if a==2:
    #Ejercicio2
    estado= 0 #0 par, 1 impar
    num=int(input("Ingrese un numero o -1 para terminar: "))
    if num!=-1:
        while num!=-1:
            estado= 1-0
            num=int(input("Ingrese un numero o -1 para terminar: "))
        if estado==0:
            print("El numero es par.")
        elif estado ==1:
            print("El numero es impar.")
    else:
        print("Error, ingrese un valor válido.")

if a==4:
    #Ejercicio4
    num=42
    print("Numeros impares del 42 al 176.")
    while num <= 176:
        if num%2!=0:
            print(num)
        num=num+1

if a==5:
    #Ejercicio5
    n=int(input("Definir valor de N: "))
    num=1
    print("Los valores entre 1 y", n,"son:")
    while num <= n:
        print(num)
        num=num+1

if a==7:
    #Ejercicio7
    posicion=0
    total=0
    mayor=0
    while posicion <=10:
        num=float(input("Ingrese numero: "))
        posicion=posicion+1
        total=total+num
        if num > mayor:
            mayor=num
            pm=posicion
    promedio=total/posicion
    print("Promedio:", promedio)
    print("El numero mas grande:", mayor)
    print("La posición del numero mas grande:", pm)

if a==8:
    #Ejercicio8
    num=float(input("Ingrese un número: "))
    cantidad=1
    total=0
    if num%2==0:
        total=num
    while total < 100:
        num=float(input("Ingrese un número: "))
        if num%2==0:
            total=total+num
        cantidad=cantidad+1
    print("Se ingresaron un total de", cantidad, "numeros.")

if a==10:
    #Ejercicio10
    n=int(input("Ingrese un numero entero mayor a cero: "))
    factorial=1
    contador=n
    if n > 0:
        while contador > 1:
            factorial=factorial*contador
            contador=contador-1
        print("El resultado factorial de", n, "es:", factorial)
    else:
        print("Error, ingresa un numero valido.")

if a==11:
    #Ejercicio11
    h=int(input("Indique un numero natural: "))
    raiz=h**(1/2)
    divisor=0
    while divisor < raiz:
        divisor=divisor+1
        if h%divisor==0 and divisor!=h and divisor!=1:
            print("El numero no es primo.")
            divisor=raiz
    if divisor!=raiz:
        print("El numero es primo.")

if a==12:
    #Ejercicio12
    n=int(input("Ingrese un número: "))
    fib=0
    fib2=0
    vfib=1
    total=0
    print("Los numeros que se presentan en la sucesión de Fibonacci antes de", n, "son:")
    while fib <= n:
        total=total+fib
        print(fib)
        fib=fib2+vfib
        fib2=vfib
        vfib=fib
    print("")
    print("Además, si sumamos todos estos números nos da el resultado de", total)
