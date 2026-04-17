selector=int(input("Ingrese un ejercicio del 1 al 10: "))

#Ejercicio1
n1 = int(input("ingresar numero 1: "))
n2 = int(input("ingresar numero 2: "))
if n1 == n2:
    print("son iguales.")
else:
    print("son distintos.")
    
#Ejercicio2
num = int(input("Ingrese un numero entero: "))
num = num%2
if num == 0:
    print("el numero es par.")
else:
    print("el numero es impar.")
    
#Ejercicio3
m = int(input("Ingrese un mes: "))
if m >= 1 and m <= 12:
    if m==1:
        print("El mes es enero.")
    elif m==2:
        print("El mes es febrero.")
    elif m==3:
        print("El mes es marzo.")
    elif m==4:
        print("El mes es abril.")
    elif m==5:
        print("El mes es mayo.")
    elif m==6:
        print("El mes es junio.")
    elif m==7:
        print("El mes es julio.")
    elif m==8:
        print("El mes es agosto.")
    elif m==9:
        print("El mes es septiembre.")
    elif m==10:
        print("El mes es octubre.")
    elif m==11:
        print("El mes es noviembre.")
    elif m==12:
        print("El mes es diciembre.")
else:
    print("No es un mes valido.")

#Ejercicio4
si = int(input("Ingrese votos a favor: "))
no = int(input("Ingrese votos en contra: "))
total = si+no
si2 = si
no2 = no
if si != 0:
    si = si/total*100
if no != 0:
    no = no/total*100
si = str(si) + "%"
no = str(no) + "%"
print("")
print("Porcentaje de votos a favor: ", si)
print("Porcentaje de votos en contra: ", no)
if si > no:
    print("Se aprueba la ley.")
else:
    print("Se rechaza la ley.")
    
#Ejercicio5
uno = float(input("Ingrese la calificacion del alumno en el primer parcial: "))
if uno >= 0 and uno <= 10: #Detectamos si nota uno es valida
    dos = float(input("Ingrese la calificacion del alumno en el segundo parcial: ")) #Detectamos si nota dos es valida tambien
    if dos >= 0 and dos <= 10: 
        if uno >= 4 and dos >= 4:
            print("el alumno aprobó los dos parciales") #Si las dos notas son mayores a cuatro es porque esta aprobado.
            if uno >= 7 and dos >= 7:
                print("el alumno promocionó.") #Si ademas de cumplir el aprobado, sus dos notas son mayores a 7 es porque promociona.
        elif uno < 4 and dos < 4: #Si no sucede el primer if de aprobado se verifica si desaprobo los dos
            print("el alumno desaprobó los dos parciales y perdió la oportunidad de recuperar.")
        elif uno < 4: #Si no desaprobo los dos, es porque desaprobo uno solo, el cual debemos verificar cual es
            print("el alumno debe recuperar el primer parcial.")
        else:
            print("el alumno debe recuperar el segundo parcial.")
    else: #En caso de que no se cumpla el if de numeros de nota dos valida, da un error
        print("Error, no es una nota valida.")
else: #En caso de que no se cumpla el if de numeros de nota uno valida, da un error
    print("Error, no es una nota valida.")

#Ejercicio6
pag = int(input("Ingresa la cantidad de páginas del libro: "))
libro = 5000+(32*pag)
if pag > 300:
    libro = libro+1200
if pag > 600:
    libro = libro+3360
print("El precio del libro será de:", libro)

#Ejercicio7
km = float(input("Ingrese cantidad de kilometros a recorrer: "))
km1 = km
min = 2700
if km >= 0 and km <= 10:
    km = 400*km
elif km > 10:
    km = 200*km
if km < 2700:
    km = min
km = str(km)
km1 = str(km1)
print("Ante el recorrido de " + km1 + "kms, el precio del viaje será de: $" + km)

#Ejercicio8
año = int(input("Ingrese un año: "))
if año%4==0 and ((año%400==0) or (not año%100==0)):
    print(año, "es bisiesto.")
elif (año%4==0 and año%100==0) or año!=0:
    print(año, "no es bisiesto.")

#Ejercicio9
d = int(input("Ingrese el día: "))
m = int(input("Ingrese el mes: "))
a = int(input("Ingrese el año: "))
actual = 2026
bi = 0
#Verificacion año bisiesto
if a >= 1 and a <= actual:
    if a%4==0 and ((a%400==0) or (not a%100==0)):
        bi = True
    elif (a%4==0 and a%100==0) or a!=0:
        bi = False
#Verificacion mes
    if (m >= 1 and m <= 12):
        if ((m >= 1 and m <= 6) and ((m%2)!=0)) or (m >= 7 and m <= 12) and ((m%2)==0): #Meses con 31 dias
            if d >= 1 and d <= 31:
                print("La fecha es valida.")
            else:
                print("Error, fecha incorrecta.")
        elif (((m >= 1 and m <= 6) and ((m%2)==0)) or ((m >= 7 and m <= 12) and ((m%2)!=0))) and (m != 2): #meses con 30 días
            if d >= 1 and d <= 30:
                print("La fecha es valida.")
            else:
                print("Error, fecha incorrecta.")
        elif m == 2: #Mes de febrero
            if bi == True: #Si es bisiesto
                if d >= 1 and d <= 29:
                    print("La fecha es valida.")
                else:
                    print("Error, fecha incorrecta.")
            elif bi == False: #Si no es bisiesto
                if d >= 1 and d <= 28:
                    print("La fecha es valida.")
                else:
                    print("Error, fecha incorrecta.")
            else:
                print("Error, fecha incorrecta.")
    else:
        print("Error, fecha incorrecta.")
else:
    print("Error, fecha incorrecta.")
    
#Ejercicio10
basico = float(input("Ingrese su sueldo basico: "))
antiguedad = int(input("Ingrese sus años de antigüedad: "))
estado = int(input("Ingrese ´1´ para soltero, ´2´ para casado: "))
soltero = (basico * (5/100))*antiguedad
casado = (basico * (7/100))*antiguedad
jubilacion = basico * (11/100)
social = basico * (3/100)
sindicato = basico * (3/100)
if estado == 1:
    neto = (basico+soltero) - (jubilacion+social+sindicato)
elif estado == 2:
    neto = (basico+casado) - (jubilacion+social+sindicato)
if estado >= 1 and estado <= 2:
    print("Ante el sueldo de", basico)
    if estado == 1:
        print("Por", antiguedad, "años de antiguedad y su estado civil, se la acredita la suma de", soltero)
    else:
        print("Por", antiguedad, "años de antiguedad y su estado civil, se la acredita la suma de", casado)
    print("Se le descuentan:")
    print("-", jubilacion, "por jubilacion")
    print("-", social, "por obra social")
    print("-", sindicato, "por sindicato")
    print("En total, su SUELDO NETO es de:", neto)
else:
    print("Error, estado incorrecto.")
