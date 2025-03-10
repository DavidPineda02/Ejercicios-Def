# Que calcule el gasto de agua en una vivienda dado el número de litros gastados, siendo el sistema de cobro:  
# • La cuota fija mensual es de 600 pesos 
# • Los primeros 50 litros son gratis (opción 1)  
# • Mayor de 50 y 200 litros se cobra el litro a 1000 pesos (opción 2)  
# • Mayor de 200 litros se cobra el litro a 3000 pesos (opción 3)  
# • Indicación: hazlo con tres ‘SI’, uno por cada opción. 

def calcularGasto(cantAgua):
    cuotFija = 600

    if cantAgua >= 1 and cantAgua <= 50:
        return cuotFija
    elif cantAgua > 50 and cantAgua <= 200:
        return  + cuotFija((cantAgua - 50) * 1000)
    elif cantAgua > 200:
        return cuotFija + ((cantAgua - 50) * 3000)
    else:
        return -1

def mostrarRecibo(cantAgua, valPag):
    if valPag <= -1:
        print("\nEl Numero Ingresado es Negativo.")
        print("\n===========================================")
    else:
        print("\n----- Recibo del Agua -----")
        print(f"Cantidad Gastada: {cantAgua} litros")
        print(f"Valor a Pagar: ${valPag:,.0f}")
    print("\n===========================================")

def cobroAgua():
    print("========== Cobro de Agua Gastada ==========")
    cantAgua = int(input("\nDigite la Cantidad de Agua Gastada en Litros: "))
    valPag = calcularGasto(cantAgua)
    mostrarRecibo(cantAgua, valPag)

cobroAgua()
