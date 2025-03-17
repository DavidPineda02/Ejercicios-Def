# 9. Crear un programa que registre 50 números enteros y luego muestren los elementos que son
# múltiplos de 5, este se determina si con la fórmula de: Numero_ingresado_porteclado mod = 0.

def multiplos(lista):
    multiplos = []

    for i in range(len(lista)):
        if lista[i] %5==0:
            multiplos.append(lista[i])
    return multiplos

print("========= Multiplos de 5 ==========\n")

lista = []

for i in range(5):
    numero = int(input(f"Digite un Numero {i + 1} : "))
    lista.append(numero)

print("\n----------- Lista de Numeros----------- ")
print(f"Los Numeros son: {lista}")
print("\n----------- Lista Multiplos de 5 ----------- ")
print(f"Los Numeros son: {multiplos(lista)}")
print("\n===================================")