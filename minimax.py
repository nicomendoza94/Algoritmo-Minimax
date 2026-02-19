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
