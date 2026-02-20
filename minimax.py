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

# Funcion para mostrar la matriz    
def mostrar_matriz(gato, raton):
    os.system("cls" if os.name == "nt" else "clear")
    for fila in range(MATRIZ_TAMANO):
        linea = ""
        for columna in range(MATRIZ_TAMANO):
            pos = (fila, columna)
            if pos == gato.posicion():
                linea += "G "
            elif pos == raton.posicion():
                linea += "R "
            else:
                linea += ". "
        print(linea)
    print()

def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def evaluar_estado(gato, raton):
    dist = manhattan(gato.posicion(), raton.posicion())
    if dist == 0:
        return 1000  # gato atrapa al raton
    elif dist == 1:
        return 100   # incentivo para acercarse
    else:
        return -dist
    
def minimax_gato(gato, raton, profundidad, maximizando):
    if profundidad == 0 or gato.posicion() == raton.posicion():
        return evaluar_estado(gato, raton), gato.posicion()
    
    #turno del gato que quiere maximizar su beneficio
    if maximizando:
        mejor_valor = float("-inf")
        mejor_mov = gato.posicion()
        movimientos = gato.movimientos_permitidos()
        random.shuffle(movimientos)   # Desempatar
        for mov in movimientos:
            gato_copia = copy.deepcopy(gato)
            gato_copia.mover(*mov)

            if gato_copia.posicion() == raton.posicion():
                return 1000, mov   # captura del raton
            #se llama recurisvamente a la funcion, pero para el turno del raton
            valor, _ = minimax_gato(gato_copia, raton, profundidad - 1, False)
            if valor > mejor_valor:   #compara el valor que dio de comparar ese movimiento
                mejor_valor = valor
                mejor_mov = mov
        return mejor_valor, mejor_mov
    else:
        # El gato simula posibles movimientos aleatorios del ratón (para anticiparse)
        peor_valor = float("inf")
        peor_mov = raton.posicion()
        movimientos = raton.movimientos_permitidos()
        random.shuffle(movimientos)
        for mov in movimientos:
            raton_copia = copy.deepcopy(raton)
            raton_copia.mover(*mov)
            valor, _ = minimax_gato(gato, raton_copia, profundidad - 1, True)
            if valor < peor_valor:
                peor_valor = valor
                peor_mov = mov
        return peor_valor, peor_mov

def iniciar_juego():
    gato = Gato(0, 0, 'G')
    raton = Raton(6, 6, 'R')
    turno = 0
    Turnos_disp = 20

    while gato.posicion() != raton.posicion() and turno < Turnos_disp:
        print(f"Turno {turno + 1}/{Turnos_disp}")
        mostrar_matriz(gato, raton)
        time.sleep(1)

        if turno % 2 == 0:
            # Turno del ratón aleatorio
            movs = raton.movimientos_permitidos()
            if movs:
                raton.mover(*random.choice(movs))
        else:
            # Turno del gato con minimax
            _, mov = minimax_gato(gato, raton, profundidad=3, maximizando=True)
            gato.mover(*mov)

        turno += 1

    mostrar_matriz(gato, raton)

    if gato.posicion() == raton.posicion():
        print("El gato atrapó al ratón!")
    else:
        print("El ratón escapó tras varios turnos.")


iniciar_juego()


