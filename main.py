import random

nombre = input("¿Cuál es tu nombre?: ")

vida = 100
aura = 0
inventario = {}

print(f"¿Qué hay, {nombre}?")
print(f"Tienes {vida} puntos de vida colega.")

while True:
    print("\n--- MENÚ ---")
    print("1. Explorar")
    print("2. Ver estadísticas")
    print("3. Ver inventario")
    print("4. Salir")

    opcion = input("Elige una crack: ")

    if opcion == "1":
        print("Sales a explorar...")

        evento = random.randint(1, 6)

        if evento == 1:
            print("¡Encuentras un doble elefante telépata de guerra!")
            aura +=30
            if "Colmillo de elefante" in inventario:
                inventario["Colmillo de elefante"] += 1
            else:
                inventario["Colmillo de elefante"] = 1

            print("+30 de aura")
            print("Has conseguido un colmillo de elefante")
           

        elif evento == 2:
            print("¡Tung tung tung sahur te ataca!")
            vida -= 10
            print("-10 puntos de vida")
            print(f"Te quedan {vida} puntos de vida.")
            
            print("¡Tung tung tung sahur te desafía a un duelo mental!")

            numero_secreto = random.randint(1, 3)

            elección = input("Adivina un número del 1 al 3: ")

            if int(elección) == numero_secreto:
                print("¡Has ganado el duelo!")
                
                print("Le robas el mazo a Tung tung tung sahur")

                print("+50 de aura")

                if "Mazo de sahur" in inventario:
                    inventario["Mazo de sahur"] += 1
                else:
                    inventario["Mazo de sahur"] = 1

                    aura += 50

            else:
                print("Has perdido el duelo...")

        elif evento == 3:
            print("Un pájaro te caga encima")
            aura -=20
            print("-20 de aura")

        elif evento == 4:
            print("Te echas una siesta")
            vida +=10

            if vida > 100:
                vida = 100

            print("+10 puntos de vida")
            print(f"Tienes {vida} puntos de vida.")

            suerte = random.randint(1, 2)

            if suerte == 1:
                print("¡Has encontrado una manta vieja!")

                if "Manta vieja" in inventario:
                    inventario["Manta vieja"] += 1
                else:
                    inventario["Manta vieja"] = 1

        elif evento == 5:
            print("¡Escapando de un therian te metes en una cueva y encuentras una mina de aura!")
            aura += 100
            print("¡+100 de aura!")

        else:
            print("No ocurre nada.")

    elif opcion == "2":
        print(f"Nombre: {nombre}")
        print(f"Vida: {vida}")
        print(f"Aura: {aura}")

    elif opcion == "3":
        if len(inventario) == 0:
            print("No tienes nada")
        else:
            print("Inventario")

            for objeto, cantidad in inventario.items():
                print(f"{objeto} x{cantidad}")

    elif opcion == "4":
        print("Hasta la próxima")
        break

    else:
        print("Opción no válida.")
    if vida <= 0:
        print("La has palmado. Fin del juego.")
        break

    if aura >= 500:
        print("Tienes +500 de aura, te has convertido en el ser más basado del universo.")
        print("¡HAS GANADO!")
        break
