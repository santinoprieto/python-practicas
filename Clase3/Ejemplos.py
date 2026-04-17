#Clase3
#Ejemplo1
numero = float(input("Ingrese un numero entero: "))
if numero > 5:
    print("el numero", numero, "es mayor a 5.")

#Ejemplo2
nota = int(input("Calificación del alumno: "))
if nota >= 4:
    print("El alumno aprobó")
else:
    print("El alumno desaprobó")
    
#Ejemplo3
n = float(input("Ingrese un numero: "))
if n == 0:
    print(n, "es cero.")
elif n > 0:
    print(n, "es positivo.")
else:
    print(n, "es negativo.")
    
#Ejemplo4
mes = int(input("Ingrese un numero: "))
if mes >= 1 and mes <= 12:
    print("el mes es valido.")
else:
    print("el mes es invalido.")