import sqlite3
from sqlite3 import Error
import random
from Clases import *
import getpass

# Función Conexión
def conexion():
    try:
        con = sqlite3.connect("Estadisticas.db")
        return con
    except Error:
        print("No se pudo conectar con la base de datos")


#Instancias Clases
Jugadores = EstadisticasJugador(conexion())
Jugador = EstadisticasSoloJugador(conexion())


# Función Creación de Tabla de Estadísticas
def Estadísticas(con):
    cursor=con.cursor()
    Query="CREATE TABLE IF NOT EXISTS ESTADISTICAS( "
    Query+="ID VARCHAR (5), "
    Query+="JUGADORES VARCHAR (5), "
    Query+="INTENTOS INT,"
    Query+="TOQUES INT,"
    Query+="FAMAS INT,"
    Query+="NADAS INT,"
    Query+="POTEN_01 BLOB,"
    Query+="POTEN_02 BLOB)"
    cursor.execute(Query)
    con.commit()

# Función aumento de intentos
def aumento_intentos(id,con):
    cursor=con.cursor()

    Query="UPDATE ESTADISTICAS "
    Query+=f"SET INTENTOS = INTENTOS + 1 WHERE ID = {id};"
    cursor.execute(Query)

    Query_toques="UPDATE ESTADISTICAS "
    Query_toques+=(f"SET POTEN_01 = True WHERE ID = {id} AND INTENTOS = 5 AND TOQUES < 10;")
    cursor.execute(Query_toques)

    Query_toques="UPDATE ESTADISTICAS "
    Query_toques+=(f"SET POTEN_02 = True WHERE ID = {id} AND INTENTOS = 10 AND TOQUES < 15;")
    cursor.execute(Query_toques)

    con.commit()


# Función Ingreso Toques, Famas y Nadas
def aumento_estadisticas(toques,famas,nadas,id,con):
    cursor=con.cursor()

    Query_toques="UPDATE ESTADISTICAS "
    Query_toques+=(f"SET TOQUES = TOQUES + {toques} WHERE ID = {id};")
    cursor.execute(Query_toques)

    Query_famas = "UPDATE ESTADISTICAS "
    Query_famas+=(f"SET FAMAS = FAMAS + {famas} WHERE ID = {id};")
    cursor.execute(Query_famas)

    Query_nadas = "UPDATE ESTADISTICAS "
    Query_nadas+=(f"SET NADAS = NADAS + {nadas} WHERE ID = {id};")
    cursor.execute(Query_nadas)

    con.commit()

#Funcion obtener número 4 dígitos
def obt_4_digitos():
    num = input("Ingrese un número de 4 dígitos sin que estos se repitan --> ")
    while len(set(num)) != 4:
        num = input("INGRESE un NÚMERO DE 4 DÍGITOS --> ")
    return num

#Menu Jugador:
def menu(id,n,con):
    print("MENU")
    diccionario_02 = {"1":"Ingresar número","2":"Inventario","3":"Historial de jugadas"}
    for x,y in diccionario_02.items():
        print(f">{x}--> {y}")
    opc_02 = input("--> ")

    while opc_02 not in diccionario_02.keys():
        opc_02 = input("--> ")

    if opc_02 == "1":
        terminator = adivinanza(id,n)

    if opc_02 == "2":
        terminator = inventario(id, n, con)

    if opc_02 == "3":
        terminator = historial(id,n,con)

    return terminator


#Funcion comprobar
def adivinanza(id,n):
    toques = 0
    famas = 0
    adv_juego = obt_4_digitos()

    #Encontrar Famas
    for x in range (0,4):
        if adv_juego[x] == n[x]:
            famas += 1

    #Encontrar Toques
    for y in adv_juego:
        if y in n:
            toques += 1
    toques -= famas

    #Encontrar Nadas
    nadas = 4 - (toques + famas)

    if famas != 4:
        with open (f"{id}.txt", "a") as archivo:
            archivo.write(f"{adv_juego} --> ¬Toques--> {toques} ; ¬Famas--> {famas} ; ¬Nadas--> {nadas}\n")
        print(f"¬Toques--> {toques}\n¬Famas--> {famas}\n¬Nadas--> {nadas}")
        aumento_intentos(id,conexion())
        aumento_estadisticas(toques,famas,nadas,id,conexion())
        terminator = False

    else:
        print("Felicidades, usted GANÓ EL JUEGO")
        aumento_intentos(id,conexion())
        aumento_estadisticas(toques,famas,nadas,id,conexion())
        terminator = True
    return terminator

#Funcion Inventario
def inventario(id,n, con):
    print("INVENTARIO")
    cursor = con.cursor()
    diccionario = {"0": "Regresar"}

    verify_01 = f"SELECT POTEN_01 FROM ESTADISTICAS WHERE ID = {id};"
    cursor.execute(verify_01)
    result_01 = cursor.fetchone()
    if result_01 and result_01[0]:
        diccionario["1"] = "Obtener un elemento al azar del número"

    verify_02 = f"SELECT POTEN_02 FROM ESTADISTICAS WHERE ID = {id};"
    cursor.execute(verify_02)
    result_02 = cursor.fetchone()
    if result_02 and result_02[0]:
        diccionario["2"] = "Obtener el n elemento del número"

    for x, y in diccionario.items():
        print(f">{x} ---> {y}")

    opc = input("Ingrese un aumento a usar--> ")
    while opc not in diccionario.keys():
        opc = input("Opción no encontrada --> ")

    if opc == "0":
        terminator = menu(id,n,con)

    elif opc == "1":
        numero = random.randint(0,3)
        print(f"Número --> {n[numero]}")
        Query_eliminar = "UPDATE ESTADISTICAS "
        Query_eliminar += (f"SET POTEN_01 = 0 WHERE ID = {id};")
        cursor.execute(Query_eliminar)
        con.commit()
        del diccionario["1"]
        terminator = False

    elif opc == "2":
        pos = int(input("Ingrese la posición a encontrar--> "))
        while pos>3 or pos<0:
            pos = int(input("Posición inválida--> "))
        print(f"Número de posición {pos} --> {n[pos]}")
        Query_eliminar = "UPDATE ESTADISTICAS "
        Query_eliminar += (f"SET POTEN_02 = 0 WHERE ID = {id};")
        cursor.execute(Query_eliminar)
        con.commit()
        del diccionario["2"]
        terminator = False

    return terminator

def obt_4_machine():
    while True:
        numero = ''.join(random.sample('0123456789', 4))
        return numero


def base():
    Estadísticas(conexion())
    Jugadores.eliminar_estadisticas()
    Jugadores.insercion_estadisticas_normal()

def base_02():
    Estadísticas(conexion())
    Jugador.eliminar_estadisticas()
    Jugador.insercion_estadisticas_uno()

def separacion():
    for x in range(0,40):
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

def intentos(id,con):
    cursor = con.cursor()
    cursor.execute(f"SELECT INTENTOS FROM ESTADISTICAS WHERE ID = {id}")
    intentos = cursor.fetchone()[0]
    return intentos

def eliminacion(archivo):
    with open(f"{archivo}.txt","r") as file:
        lineas = file.read()
        if lineas.strip() == "":
            pass
        else:
            with open(f"{archivo}.txt","w") as file_2:
                file_2.write("")

def historial(archivo,n,con):
    with open(f"{archivo}.txt","r") as file:
        lineas = file.readlines()
        if len(lineas) == 0:
            print("No se han realizado jugadas aún.")
        else:
            for x in lineas:
                print(f"> {x.rstrip()}")

    terminator = menu(archivo, n, con)
    return terminator

def inicio():
    eliminacion(1)
    eliminacion(2)


