import sqlite3

class EstadisticasBase:
    def __init__(self, conexion):
        self.conexion = conexion

    def eliminar_estadisticas(self):
        cursor = self.conexion.cursor()
        Query = f"DELETE FROM ESTADISTICAS;"
        cursor.execute(Query)
        self.conexion.commit()

class EstadisticasJugador(EstadisticasBase):
    def __init__(self, conexion):
        super().__init__(conexion)

    def insercion_estadisticas_normal(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM ESTADISTICAS")
        validador = cursor.fetchone()
        if not validador:
            nombre_01 = input("Ingrese el nombre del Jugador 1 --> ")
            nombre_02 = input("Ingrese el nombre del Jugador 2 --> ")
            lista_datos = [("1", nombre_01, 0, 0, 0, 0, 0, 0), ("2", nombre_02, 0, 0, 0, 0, 0, 0)]
            cursor.executemany("INSERT INTO ESTADISTICAS VALUES(?,?,?,?,?,?,?,?);", lista_datos)
            self.conexion.commit()


class EstadisticasSoloJugador(EstadisticasBase):
    def __init__(self, conexion):
        super().__init__(conexion)

    def insercion_estadisticas_uno(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM ESTADISTICAS")
        validador = cursor.fetchone()
        if not validador:
            nombre_01 = input("Ingrese su nombre, Jugador 1 --> ")
            lista_datos = [("1", nombre_01, 0, 0, 0, 0, 0, 0)]
            cursor.executemany("INSERT INTO ESTADISTICAS VALUES(?,?,?,?,?,?,?,?);", lista_datos)
            self.conexion.commit()


