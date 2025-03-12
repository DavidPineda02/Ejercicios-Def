# Lorena organiza una fiesta en la cual una computadora controla el ingreso mediante 5 claves. Si  se ingresa al menos una clave incorrecta esta imprimirá "TE EQUIVOCASTE DE FIESTA" y no  permitirá el ingreso. Si las 5 claves son correctas imprimirá "BIENVENIDO A LA FIESTA" Las Claves son:  
# 1: "TIENES"  
# 2: "QUE SER"  
# 3: "INVITADO"  
# 4: "PARA"  
# 5: "INGRESAR" 

def verificar_claves():
    claves_correctas = ["TIENES", "QUE SER", "INVITADO", "PARA", "INGRESAR"]
    claves_ingresadas = []
    
    print("========== Fiesta de Lorena ==========\n")

    for i in range(5):
        clave = input(f"Ingrese la clave {i + 1}: ").upper().strip()
        claves_ingresadas.append(clave)

    if claves_ingresadas == claves_correctas:
        print("\nBIENVENIDO A LA FIESTA")
        print("\n======================================")
    else:
        print("\nTE EQUIVOCASTE DE FIESTA")
        print("\n======================================")

verificar_claves()