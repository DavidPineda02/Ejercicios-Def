# Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado. 

def superposicion(lista1, lista2):
    for x in lista1:
        for y in lista2:
            if x == y:
                return True
    return False

lista1 = []
lista2 = []
contador = 0

print("========= Superposicion en Listas =========")

while contador < 5:
    numeros1 = int(input(f"\nDigite el Numero {contador + 1} de la Primer Lista: "))
    lista1.append(numeros1)
    numeros2 = int(input(f"Digite el Numero {contador + 1} de la Segunda Lista: "))
    lista2.append(numeros2)

    contador += 1

resultado = superposicion(lista1, lista2)

print(f"\nLa Primera Lista es: {lista1}")
print(f"La Segunda Lista es: {lista2}")
print(f"\nLas Listas Tienen Elementos en Comun? {resultado}")
print("\n===========================================")