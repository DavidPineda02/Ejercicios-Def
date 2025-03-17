# Diseñe un algoritmo que determine el resultado de la elección del representante estudiantil de la  universidad X, para ello se presentaron tres candidatos A, B, y C. 
# • Para ganar la elección se debe obtener como mínimo el 51%. 
# • En caso que no haya un ganador se repite la elección en una segunda vuelta. • Van a la segunda vuelta los dos candidatos que obtengan la más alta votación. • Se anula la elección en caso de producirse un empate doble por el segundo lugar o un  empate triple.

def elecciones(votosA = 0, votosB = 0, votosC = 0):
    while True:
        print("\nDigita los Votos de cada Candidato:")
        votosA = int(input("Votos para A: "))
        votosB = int(input("Votos para B: "))
        votosC = int(input("Votos para C: "))
        
        votosTotls = votosA + votosB + votosC
        
        if votosA == votosB == votosC:
            print("\nEleccion Anulada por Empate Triple.")
            print("\n===========================================================")
            print(" ")
            break

        portjA = (votosA / votosTotls) * 100
        portjB = (votosB / votosTotls) * 100
        portjC = (votosC / votosTotls) * 100
        
        if portjA > 50:
            print(f"\nEl Ganador es A en la Primera Vuelta con {portjA}%")
            print("\n===========================================================")
            print(" ")
            break
        elif portjB > 50:
            print(f"\nEl Ganador es B en la Primera Vuelta con {portjB}%")
            print("\n===========================================================")
            print(" ")
            break
        elif portjC > 50:
            print(f"\nEl Ganador es C en la Primera Vuelta con {portjC}%")
            print("\n===========================================================")
            print(" ")
            break
        
        if (votosA == votosB and votosA > votosC) or (votosB == votosC and votosB > votosA) or (votosA == votosC and votosA > votosB):
            print("\nElecciOn Anulada por Empate Doble en el Segundo Lugar.")
            print("\n===========================================================")
            print(" ")
            break

        if votosA > votosB and votosA > votosC:
            if votosB > votosC:
                cand1 = "A"
                cand2 = "B"
            else:
                cand1 = "A"
                cand2 = "C"
        elif votosB > votosA and votosB > votosC:
            if votosA > votosC:
                cand1 = "B"
                cand2 = "A"
            else:
                cand1 = "B"
                cand2 = "C"
        else:
            if votosA > votosB:
                cand1 = "C"
                cand2 = "A"
            else:
                cand1 = "C"
                cand2 = "B"
        
        print(f"\nSegunda Vuelta entre {cand1} y {cand2}")
        votosCand1 = 0
        votosCand2 = 0

        while True:
            votosCand1 = int(input(f"\nDigite los votos para {cand1}: "))
            votosCand2 = int(input(f"Digite los votos para {cand2}: "))
            
            votosTotls2 = votosCand1 + votosCand2
            
            if votosCand1 == votosCand2:
                print("\nElección anulada por empate en segunda vuelta.")
                print("\n===========================================================")
                print(" ")
                break
            
            portjCand1 = (votosCand1 / votosTotls2) * 100
            portjCand2 = (votosCand2 / votosTotls2) * 100
            
            if portjCand1 > portjCand2:
                print(f"\nEl Ganador es {cand1} con {portjCand1:.2f}%")
                print("\n===========================================================")
                print(" ")
            else:
                print(f"\nEl Ganador es {cand2} con {portjCand2:.2f}%")
                print("\n===========================================================")
                print(" ")
            break
        break

print(" ")
print("========== ELECCION DE REPRESENTANTE ESTUDIANTIL ==========")
elecciones()