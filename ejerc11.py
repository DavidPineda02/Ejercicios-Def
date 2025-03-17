# Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te  devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además, recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login  incremente este valor. Crear un programa principal donde se pida un nombre de usuario y una  contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo. 

def Login(nomUser , pswUser , intentos):
    userVald = "usuario1"
    pswVald = "asdasd"

    if nomUser  == userVald and pswUser  == pswVald:
        return True
    else:
        intentos += 1
        return False, intentos

def main():
    print("========== Inicio de Sesión ==========")
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        nomUser  = input("\nDigite su Nombre de Usuario: ")
        pswUser  = input("Digite su Contraseña: ")

        resultado = Login(nomUser , pswUser , intentos)

        if resultado is True:
            print("\nInicio de Sesión Exitoso.")
            print("\n=======================================")
            break
        else:
            intentos = resultado[1]
            if intentos < max_intentos:
                print(f"\nCredenciales incorrectas. Intento {intentos} de {max_intentos}.")
            else:
                print("\nNumero Maximo de Intentos Alcanzado. Acceso denegado.")

main()