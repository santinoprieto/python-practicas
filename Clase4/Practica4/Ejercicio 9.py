#Ejercicio9
patente=int(input("Ultimo numero de patente o -1 para terminar: "))
par=0
impar=0
if patente!=-1:
    while patente !=-1: #Comienzo de ciclo
        if patente >= 0 and patente <= 9: #Verificación de numeración correcta
            if (patente%2)==0: #Formula para verificar par/impar
                par = par+1
            else:
                impar = impar+1
        else:
            print("Error, ingrese un número válido.")
        patente=int(input("Numero de patente(entre 0 y 9) o -1 para terminar: "))
else:
    print("Error, ingrese un número válido.")
print(par, "vehículos pasaron con numeración par")
print(impar, "vehículos pasaron con numeración impar.")