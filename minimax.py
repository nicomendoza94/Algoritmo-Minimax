import os
import time
import copy
import random

# Direcciones posibles: arriba, abajo, izquierda, derecha
DIRECCIONES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Tamaño del tablero
MATRIZ_TAMANO = 7

# Clase base que representa una entidad dentro del tablero
class Jugadores:
    def __init__(self, fila, columna, simbolo):
        self.fila = fila
        self.columna = columna
        self.simbolo = simbolo

    def mover(self, fila, columna):    #para actualizar la posición del jugador
        self.fila = fila
        self.columna = columna

    def posicion(self):   #para devolver la posicion actual
        return self.fila, self.columna
    
# Representa al jugador que intenta atrapar al ratón
class Gato(Jugadores):
    def movimientos_permitidos(self):
        movimientos = []

        for cambio_f, cambio_c in DIRECCIONES:
            nueva_f, nueva_c = self.fila + cambio_f, self.columna + cambio_c

            if 0 <= nueva_f < MATRIZ_TAMANO and 0 <= nueva_c < MATRIZ_TAMANO:
                movimientos.append((nueva_f, nueva_c))
        return movimientos

# Representa al jugador que intenta escapar del gato
class Raton(Jugadores):
    def movimientos_permitidos(self):
        movimientos = []

        for cambio_f, cambio_c in DIRECCIONES:
            nueva_f, nueva_c = self.fila + cambio_f, self.columna + cambio_c

            if 0 <= nueva_f < MATRIZ_TAMANO and 0 <= nueva_c < MATRIZ_TAMANO:
                movimientos.append((nueva_f, nueva_c))
        return movimientos
