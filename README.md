# Estructuras de Datos y Algoritmos

Simulador en Python de usuarios que se mueven por un plano y avisan a sus vecinos cercanos. Hay una versión inicial con listas y otra optimizada con un Quadtree propio.

> Asignatura **Estructuras de Datos y Algoritmos** · 2º curso, 1º cuatrimestre · curso 2022-2023 · Grado en Ingeniería Informática, Universidad de Valladolid.

## Qué hace

- Lee un fichero de estado inicial con cada usuario: identificador, coordenadas `x y`, grupo y lista de vecinos.
- Aplica un fichero de movimientos y recalcula qué usuarios quedan dentro de la zona de control (radio 2.0).
- Genera los mensajes de entrada y salida de vecinos: `A-B` cuando B sale de la zona, `A+=B` cuando entra uno del mismo grupo y `A+/B` cuando entra uno de otro grupo.
- **Modo depuración (`D`):** procesa los movimientos del fichero, muestra el tiempo empleado y produce los mensajes.
- **Modo medición (`M`):** genera movimientos aleatorios durante N ciclos y muestra el tiempo de cada ciclo y la media.

## Tecnologías

- Python 3 (solo biblioteca estándar: `math`, `random`, `time`)

## Aspectos técnicos destacados

- **Práctica 1:** cada `Usuario` busca sus vecinos recorriendo a todos los demás y calculando la distancia euclídea, es decir, una búsqueda O(n) por usuario.
- **Práctica 2:** `Arbol_de_0.py` implementa un **Quadtree** desde cero (clases `Punto`, `Rectangulo` y `Quadtree`, con capacidad 4 por nodo). Ofrece inserción recursiva, subdivisión en cuatro cuadrantes, eliminación de un punto y búsqueda por radio limitada a las regiones que intersecan con la zona de control.
- En cada movimiento, el usuario se elimina del árbol con sus coordenadas antiguas y se vuelve a insertar con las nuevas. Los límites del árbol se calculan a partir del máximo de `x` e `y` entre el estado inicial y los movimientos.
- Los usuarios se guardan en un diccionario indexado por identificador, así que encontrar el usuario de cada movimiento no exige recorrer una lista.
- `sin_mejorar.py` conserva la versión de referencia con búsqueda lineal para comparar. En una ejecución local con `inicial_14000_1.0_.txt` (medición no oficial), la versión con Quadtree tardó unos 0,65 s y la de referencia unos 47 s.
- Los análisis de rendimiento entregados están en [`Practica1/ENTREGA/analisis.pdf`](Practica1/ENTREGA/analisis.pdf) y [`Practica2/ENTREGA/analisis.pdf`](Practica2/ENTREGA/analisis.pdf).

## Estructura del repositorio

```
EDA/
├── Practica1/
│   ├── practica.py        # programa principal (modos D y M)
│   ├── usuarios.py        # clase Usuario y búsqueda de vecinos
│   ├── ficheros/          # ficheros de estado, movimientos y mensajes de prueba
│   ├── ENTREGA/           # análisis y código entregado
│   └── DEFENSA/           # versión y ficheros usados en la defensa
└── Practica2/
    ├── p2223_1.py         # programa principal con Quadtree
    ├── Arbol_de_0.py      # implementación del Quadtree
    ├── sin_mejorar.py     # versión de referencia sin Quadtree
    ├── comprobacion.py    # script auxiliar que compara ficheros de mensajes
    ├── *_14000_*.txt, *_50000_*.txt   # ficheros de prueba
    ├── ENTREGA/
    └── DEFENSA/
```

## Requisitos

- Python 3.6 o superior (la práctica 2 usa f-strings)

## Cómo compilar y ejecutar

Los programas son interactivos: piden el nombre del fichero de estado, el modo y, en modo depuración, el fichero de movimientos. Los parámetros `n` y `d` se extraen del nombre del fichero (`inicial_<n>_<d>_.txt`), así que hay que conservar ese formato.

Práctica 1 (se ejecuta desde su carpeta, porque importa `usuarios.py`):

```bash
cd Practica1
python3 practica.py
# Fichero de estado: ficheros/inicial_10_1.0_.txt
# Modo [D]epuracion o [M]edicion? D
# Fichero de movimientos: ficheros/movs_10_0.4_.txt
```

Práctica 2:

```bash
cd Practica2
python3 p2223_1.py
# Fichero de estado: inicial_14000_1.0_.txt
# Modo [D]epuración o [M]edición? D
# Fichero de movimientos:        (en blanco se usa movs_14000_1.0_.txt)
```

En modo depuración, la práctica 2 escribe los mensajes en `msgs_<n>_<d>_.txt`, en el directorio actual, y sobrescribe el que haya. Ambas ejecuciones se han probado con Python 3 sobre una copia del repositorio.

## Autoría

Trabajo en pareja (subgrupo de laboratorio K2). Según la cabecera del código, sus autores son Javier García González y Azael Bastardo Rodríguez.

---

Forma parte de [UVa-Projects](https://github.com/JavivuG/UVa-Projects).
