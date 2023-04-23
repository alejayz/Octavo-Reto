#3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

x = int(input("ingrese un número mayor o igual a 2: ")) # se debe ingresar un número entero
if x % 2 != 0: #se utiliza el operador de igualdad para saber si el número es par
    x -= 1 #si no es par se resta 1 para arrojar secuencia de pares
for i in range(x,0,-2): #se indica el rango a imprimir y se utilixa -2 para arrojar secuencia de pares
        print(i)
