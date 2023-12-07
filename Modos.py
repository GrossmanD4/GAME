from Funciones import *

def one_vs_one():
    base()

    print("> Jugador 01:")
    J1 = obt_4_digitos()
    separacion()

    print("> Jugador 02:")
    J2 = obt_4_digitos()
    separacion()

    while True:
        print("Jugador 01:")
        terminator = menu("1", J2, conexion())
        print("-------------------------------------------------")
        if terminator:
            print("Jugador 01 ha ganado. ¡Felicidades!")
            intento = intentos("1",conexion())
            print(f"Le tomó {intento} intento/s.")
            break

        print("Jugador 02:")
        terminator = menu("2", J1, conexion())
        print("-------------------------------------------------")
        if terminator:
            print("Jugador 02 ha ganado. ¡Felicidades!")
            intento = intentos("2",conexion())
            print(f"Le tomó {intento} intento/s.")
            break

    # Agregamos este mensaje fuera del bucle
    print("El juego ha terminado.")

def one_vs_machine():
    base_02()

    machine = obt_4_machine()
    print(machine)


    while True:
        print("> Jugador 01:")
        terminator = menu("1", machine, conexion())
        print(terminator)
        print("-------------------------------------------------")
        if terminator:
            print("Ha ganado. ¡Felicidades!")
            intento = intentos("1",conexion())
            print(f"Le tomó {intento} intento/s.")
            break

    print("El juego ha terminado.")

def creditos():
    print("  ------------------------------------------  ")
    print("--Elaborado por Grossman Miguel Vargas Pérez--")
    print("--         Trabajo Final Curso LP           --")
    print("-- En agradecimiento a mis padres y hermana --")
    print("  ------------------------------------------  ")

def reglas():
    print("  ----------------Pica y Fama---------------  ")
    print("  1. Por parte del modo JcJ ambos jugadores indicarán su número de 4 dígitos, el cual no debe contar con números repetidos,")
    print("     evitando así ciertas técnicas ingeniosas que dificulten la experiencia de juego.")
    print("  2. Tras ello, el jugador empezará a tratar de adivinar el número del rival, para lo cual contamos con 3 tipos de estadísticas")
    print("     que nos ayudarán, estas son: ")
    print("         > Las FAMAS  --> Dígito que se encuentra en el número en la posición acertada.")
    print("         > Los TOQUES --> Dígito que se encuentra en el número pero no en la posición acertada.")
    print("         > Las NADAS  --> Dígito que no se encuentra en el número.")
    print("  3. Todo esto ayudará a la complejidad del juego, al poder ir comprobando con los números de toques y famas que número pertenece y que no pertenece")
    print("  4. Usted con el pasar del tiempo y segun la evaluación del juego podrá ir adquiriendo potenciadores que aligerarán en cierta parte la búsqueda del número")
    print("     además de contar con una opcion que le permitirá revisar el historial de jugadas con la cantidad de Famas, Toques y Nadas de cada intento.")
    print("  -----------DISFRUTE SU PARTIDA!!----------")
    print("  ------------------------------------------  ")