# Algoritmo Calcular la factorial de un número N.

def calcularFactorial(n):
    if n < 0:
        return "El Numero Ingresado es Negativo."
    elif n == 0:
        return 1
    else:
        numeros = []
        for i in range(1, n + 1):
            numeros.append(i)
        
        factorial = 1
        while numeros:
            factorial *= numeros.pop()
        
        return factorial

print("========== Numero Factorial ==========")
num = int(input("\nDigite un Numero para Calcular su Factorial: "))
resultado = calcularFactorial(num)

print(f"El Factorial de {num} es: {resultado}")
print("\n======================================")