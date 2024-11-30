from model.database.DaoInterfaz import DaoInterfaz
from model.database.Singleton import Database
from model.database.Usuario import Usuario


class AbmUsuario(DaoInterfaz):
    def __init__(self) -> None:
        self.__database = Database()
        self.__database.connect()

    def validar_nombre(self, nombre):
        if self.__database.execute_query(
            "SELECT * FROM usuario WHERE nombre_usuario = ?",
            (nombre,),
        ):
            self.__database.execute_non_query(
                "UPDATE usuario SET baja_usuario = 0 WHERE nombre_usuario = ?",
                (nombre,),
            )
            return True

    def get_por_usuario(self, usuario):
        resultado = self.__database.execute_query(
            "SELECT * FROM usuario WHERE nombre_usuario = ? AND baja_usuario = 0",
            (usuario,),
        )
        if (
            not resultado
        ):  # Si no se encontro la id o esta dado de baja, devuelve una lista vacia(Aunque solo busques un usuario) y se imprime un mensaje.
            print(
                f"No se encontró el usuario con el nombre: {usuario}, o está dado de baja"
            )
            return None
        else:
            return Usuario(
                resultado[0][0],
                resultado[0][1],
                resultado[0][2],
                resultado[0][3],
                resultado[0][4],
                resultado[0][5],
            )

    def get_por_id(self, id: int) -> None | Usuario:  # ESTO ANDA
        resultado = self.__database.execute_query(
            "SELECT * FROM usuario WHERE id_usuario = ?",
            (id,),  # Devuelve una lista de tuplas
        )
        if (
            not resultado
        ):  # Si no se encontro la id o esta dado de baja, devuelve una lista vacia(Aunque solo busques un usuario) y se imprime un mensaje.
            print(f"No se encontró el usuario con el id: {id}, o está dado de baja")
            return None
        else:
            return Usuario(
                resultado[0][0],
                resultado[0][1],
                resultado[0][2],
                resultado[0][3],
                resultado[0][4],
                resultado[0][5],
            )

    def get_all(self):  # ESTO ANDA
        jugadores = []
        resultado = self.__database.execute_query(
            "SELECT * FROM usuario WHERE baja_usuario = 0 ORDER BY score DESC LIMIT 10"  # devuelve los usuarios por score
        )
        if (
            resultado is None
        ):  # Si no se encontro la id, devuelve None y se imprime un mensaje.
            print("No se encontraron usuarios")
        else:
            for jugador in resultado:
                objeto = Usuario(
                    jugador[0],
                    jugador[1],
                    jugador[2],
                    jugador[3],
                    jugador[4],
                    jugador[5],
                )
                jugadores.append(objeto)
            return jugadores

    def insertar(self, objeto):  # ESTO ANDA
        self.__database.execute_non_query(
            "INSERT INTO usuario (id_usuario, nombre_usuario, password, admin, baja_usuario, score) VALUES (?,?,?,?,?,?)",
            (
                objeto.get_id(),
                objeto.get_nombre(),
                objeto.get_password(),
                objeto.get_admin(),
                objeto.get_baja_usuario(),
                objeto.get_score(),
            ),
        )

    def actualizar(self, objeto):  # ESTO ANDA
        self.__database.execute_non_query(
            "UPDATE usuario SET nombre_usuario = ?, password = ?, admin = ?, baja_usuario = ?, score = ? WHERE id_usuario = ?",
            (
                objeto.get_nombre(),
                objeto.get_password(),
                objeto.get_admin(),
                objeto.get_baja_usuario(),
                objeto.get_score(),
                objeto.get_id(),
            ),
        )

    def borrar(self, id):  # ESTO ANDA
        self.__database.execute_non_query(
            "UPDATE usuario SET baja_usuario = 1 WHERE id_usuario = ? AND baja_usuario = 0",
            (id,),
        )

    def close(self):  # ESTO ANDA
        self.__database.close_connection()

    def actualizar_score(self, id, score):
        self.__database.execute_non_query(
            "UPDATE usuario SET score = score + ? WHERE id_usuario = ?",
            (score, id),
        )
