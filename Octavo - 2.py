#2. Imprimir lista de impares de 1 - 999 y lista de pares de 2 - 1000

range(1,1000,2) #se utiliza 2 al final para indicar el aumento entre cada número
print("Números impares: ") #para indicar el tipo de números
for i in range(1,1000,2):
    print(i)

range(2,1001,2) #se utiliza 2 al final para indicar el aumento entre cada número
print("Numeros pares: ") #para indicar el tipo de números
for i in range(2,1001,2):
    print(i)