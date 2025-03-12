# 3. Calcular el sueldo que le corresponde al trabajador de una empresa que cobra $14.400.000 anual, el programa debe realizar los cálculos en función de los siguientes criterios:
# a. Si lleva más de 10 años en la empresa se le aplica un aumento del 10%.
# b. Si lleva menos de 10 años, pero más que 5 se le aplica un aumento del 7%.
# c. Si lleva menos de 5 años, pero más que 3 se le aplica un aumento del 5%.
# d. Si lleva menos de 3 años se le aplica un aumento del 3%.

def calcularAumento(cantAños, sueldo):
    if cantAños < 0 or sueldo < 0:
        return -1
    if cantAños > 10:
        aumtSueld = sueldo * (10 / 100)
    elif cantAños > 5:
        aumtSueld = sueldo * (7 / 100)
    elif cantAños > 3:
        aumtSueld = sueldo * (5 / 100)
    else:
        aumtSueld = sueldo * (3 / 100)

    sueldTotl = sueldo + aumtSueld
    return sueldTotl

def mostrarSueldo(sueldo, sueldTotl):
    if sueldo == -1:
        print("Los Años o el Sueldo Ingresados están en Negativo.")
        print("\n===================================")
    else:
        print(f"\nEl Sueldo del Empleado es de: {sueldTotl:,.0f}")
        print("\n===================================")

def aumentoSueldo():
    print("========== Aumento Sueldo =========")
    cantAños = int(input("\nDigite la Cantidad de Años que lleva Trabajando en la Empresa: "))
    sueldo = int(input("Digite su Sueldo Actual: "))
    result = calcularAumento(cantAños, sueldo)
    mostrarSueldo(sueldo, result)

aumentoSueldo()