cant=0
total=0
num=int(input("Ingresa un numero o -1 para terminar: "))
while num!=-1:
    total = total+num
    cant = cant+1
    num=int(input("Ingresa un numero o -1 para terminar: "))
if cant!=0:
    print("El promedio es:", total/cant)
else:
    print("Error, no se ingresaron valores.")
    
#Nuevo ejemplo
n = int(input("Ingrese un número o -1 para terminar: "))
mayor = n
while n != -1:
    if n > mayor:
        mayor = n
    n=int(input("Ingrese un número o -1 para terminar: "))
print("El mayor es", mayor)