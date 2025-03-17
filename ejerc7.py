# Diseñar un pseudocódigo que calcule el promedio ponderado para alumno del ITT. El cálculo se hace de la siguiente forma: Se multiplica cada calificación por los créditos de cada materia El resultado anterior se suma con los resultados de todas las materias, por separado se suman  los créditos de cada materia y finalmente se divide la suma de todas las materias por sus  respectivos créditos, entre la suma de todos los créditos. (materias: Fundamentos, BD y ética).

def promedio(prod = 0, cred = 0, contador =0):
    while contador < len(materias):
        print(f"\nMateria: {materias[contador]}")

        calificacion = float(input(f"Digita la Nota para {materias[contador]}: "))
        creditos = int(input(f"Digita los Creditos de {materias[contador]}: "))

        prod += calificacion * creditos
        cred += creditos
        contador += 1

    prom = prod / cred
    print(f"\nEl promedio Ponderado es: {prom:.2f}")

materias = ["Fundamentos", "BD", "Ética"]
promedio()