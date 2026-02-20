# 🐱🧀 Minimax: Gato vs Ratón

Simulación en consola de un juego entre un gato y un ratón sobre una matriz 7x7.

El gato utiliza el algoritmo **Minimax** con una función heurística basada en distancia Manhattan para intentar atrapar al ratón.  
El ratón se mueve de manera aleatoria.

---

## 🎯 Objetivo del proyecto

Implementar desde cero:

- Programación orientada a objetos
- Movimiento en grilla
- Heurística basada en distancia Manhattan
- Algoritmo Minimax con profundidad limitada
- Simulación por turnos en consola

---

## 🧠 Lógica del juego

- El tablero es una matriz 7x7.
- El gato comienza en la esquina superior izquierda `(0, 0)`.
- El ratón comienza en la esquina inferior derecha `(6, 6)`.
- El ratón se mueve aleatoriamente.
- El gato utiliza Minimax para decidir su mejor movimiento.
- El juego termina cuando:
  - El gato atrapa al ratón
  - Se alcanza el límite máximo de turnos

---

## 📐 Heurística utilizada

Se usa la **distancia Manhattan**:

```
|x1 - x2| + |y1 - y2|
```

La función de evaluación:

- `1000` → el gato captura al ratón
- `100` → el gato está a una casilla
- `-distancia` → penaliza estar lejos

---

## ⚙️ Tecnologías usadas

- Python 3
- copy.deepcopy para simular estados
- random para desempate y movimientos del ratón
- os.system para limpiar la consola

---

## ▶️ Cómo ejecutar

Desde la carpeta raíz del proyecto:

```bash
python src/game.py
```

---

## 📌 Conceptos aplicados

- Programación orientada a objetos
- Algoritmos de búsqueda adversarial
- Simulación por turnos
- Diseño incremental por commits
