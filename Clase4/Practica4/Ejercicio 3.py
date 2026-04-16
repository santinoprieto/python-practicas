#Ejercicio3
n=int(input("Ingresa un número o -1 para terminar: "))
menor=n
mayor=n
while n!=-1:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n
    n=int(input("Ingresa un número o -1 para terminar: "))
if menor!=-1 and mayor!=-1: #Si no se inicio con -1(no se ingresaron numeros) deberia dar bien
    print("El mayor es", mayor, "y el menor es", menor)
else: #En caso de que no se hayan ingresado numeros
    print("Error, ingrese un número válido.")