#Ejercicio6
num = float(input("Ingrese número a multiplicar: "))
multiplicacion = 1
print("tabla del", num)
while multiplicacion <= 12:
    total = num*multiplicacion
    print(num, "*", multiplicacion, "=", total)
    multiplicacion = multiplicacion + 1