# Construya los algoritmos que permitan calcular las siguientes series con un valor de N ingresado  desde teclado: 
# • 1^2 + 2^2 + 3^2 +…N^2 tal que N es positivo 
# • 1^1 + 2^2 + 3^3 +…N^n tal que N es positivo 

def primerSecuencia(n):
    if n < 1:
        return "El Numero Debe ser Positivo."
    
    cuadrados = []
    
    for i in range(1, n + 1):
        cuadrados.append(i ** 2)

    suma = 0
    for cuadrado in cuadrados:
        suma += cuadrado
    
    return suma

def segundaSecuencia(n):
    if n < 1:
        return "El Numero Debe ser Positivo."

    cubos = []

    for i in range(1, n + 1):
        cubos.append(i ** i)

    suma = 0
    for cubo in cubos:
        suma += cubo
    
    return suma

print("========== Calculo de Series ==========")

numero = int(input("\nDigite un Numero Positivo: "))

resultCuad = primerSecuencia(numero)
resultCub = segundaSecuencia(numero)

print(f"\nSuma de la Primera Serie (1² + 2² + ... + {numero}²): {resultCuad}")
print(f"Suma de la Segunda Serie (1¹ + 2² + ... + {numero}^{numero}): {resultCub}")
print("\n=======================================")