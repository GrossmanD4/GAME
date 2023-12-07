from Modos import *
def main():
    inicio()
    print("--- MODOS DE JUEGO ---")
    dicc = {"1":"Jugador contra Jugador", "2":"Jugador contra la máquina", "3":"Créditos",  "4":"Reglas"}
    for x,y in dicc.items():
        print(f">{x} --> {y}")
    opcion = input("--> ")
    while opcion not in dicc.keys():
        opcion = input("--> ")
    if opcion == "1":
        one_vs_one()
    if opcion == "2":
        one_vs_machine()
    if opcion == "3":
        creditos()
    if opcion == "4":
        reglas()

main()