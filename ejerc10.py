listaFibonacci = []

def llenadoLista():
    print("\nSugerencia: El Numero debe ser Menor o Igual a 50.")
    numero = int(input("Digite un numero entero: "))

    def sintexisFibonacci(numero):
        if numero <= 0:
            return 0
        elif numero == 1:
            return 1
        
        f0 = 0
        f1 = 1

        for i in range(2, numero + 1):
            f0, f1 = f1, f0 + f1
        return f1

    for i in range(numero + 1):
        fx = sintexisFibonacci(i)
        listaFibonacci.append(fx)
    
    return listaFibonacci, numero

def mostrarLista(listaFibonacci, numero):
    print(f"\nLos primeros {numero} numeros de Fibonacci son: \n")

    for i, num in enumerate(listaFibonacci):
        print(f"F({i}) = {num}")

while True:
    print("\n--------- Menu ---------")
    print("\n1. Llenar Lista de Fibonacci")
    print("2. Mostrar Lista de Fibonacci")
    print("\n------------------------")

    option = int(input("\nDigite la opción que deseas: "))
    if option == 1:
        listaFibonacci, numero = llenadoLista()
    if option == 2:
        mostrarLista(listaFibonacci, numero)
        print(" ")
        break


