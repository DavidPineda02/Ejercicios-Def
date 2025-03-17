# Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y  multip([1,2,3,4]) debería devolver 24. 

def suma(listNum):
    ttlSum = 0
    for num in listNum:
        ttlSum += num

    return ttlSum

def multiplicacion(listNum):
    ttlMult = 1
    for num in listNum:
       ttlMult *= num

    return ttlMult

listNum = []
contador = 0

print("========== Multiplicacon y Suma de X Numeros ==========")

numeros = int(input("\nDigite la Cantidad de Numeros que Quiere Sumar y Multiplicar: "))
print(" ")

while contador < numeros:

    N = int(input(f"Digite el Numero {contador + 1} : "))
    listNum.append(N)

    contador += 1

resltSum = suma (listNum)
resltMult = multiplicacion(listNum)

print(f"\nLa suma es: {resltSum} ")
print(f"La Multiplicación es: {resltMult}")
print("\n=======================================================")