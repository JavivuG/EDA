import Arbol
from time import time
from random import random

RZC = 2.0       # Radio de la Zona de Control
RZC2 = RZC*RZC


class Usuario:
    def __init__(self, lin):
        self.ide, sx, sy, self.grupo, *self.vecinos = lin.split()
        self.x, self.y = float(sx), float(sy)

    def mover(self, mov):
        self.x, self.y = mov.x, mov.y

    def en_zc(self, otro):
        dx, dy = self.x - otro.x, self.y - otro.y
        return dx*dx + dy*dy < RZC2

    def mensaje(self, otro, ins):
        cod = '-' if not ins else '+=' if self.grupo == otro.grupo else '+/'
        return f"{self.ide}{cod}{otro.ide}"

class Movimiento:
    def __init__(self, ide, x, y):
        self.ide, self.x, self.y = ide, x, y

    def asigna_azar(self):
        self.x += random() - 0.5
        self.y += random() - 0.5

    @staticmethod
    def from_linea(lin):
        trozos = lin.split(' ')
        return Movimiento(trozos[0], float(trozos[1]), float(trozos[2]))

    @staticmethod
    def from_usuario(usr):
        return Movimiento(usr.ide, usr.x, usr.y)


def lee_fichero_ini(fich):
    with open(fich, 'r') as fich:
        return [Usuario(lin) for lin in fich.read().splitlines() if lin != '']

def lee_fichero_movs(fich):
    with open(fich, 'r') as fich:
        return [Movimiento.from_linea(lin) for lin in fich.read().splitlines() if lin != '']

def buscar(usrs, ide):
    if(ide in usrs):
        return usrs[ide]
    raise Exception("No existe ningún usuario con ese identificador")

def vecinos(u, arbol):
    vecs=[]
    arbol.query_radius(u.x,u.y,2,vecs)
    vecs.pop(0)
    return vecs 

def actualizar(u, vec_new, usrs, msgs):
    vec_old = u.vecinos
    # Añadir los nuevos vecinos
    for ide in vec_new:
        if ide not in vec_old:
            v = buscar(usrs, ide)
            msgs.append(u.mensaje(v, True))
            msgs.append(v.mensaje(u, True))
            v.vecinos.append(u.ide)
    # Eliminar los que ya no son vecinos
    for ide in vec_old:
        if ide not in vec_new:
            v = buscar(usrs, ide)
            msgs.append(u.mensaje(v, False))
            msgs.append(v.mensaje(u, False))
            v.vecinos.remove(u.ide)
    # Asignar la nueva lista de vecinos a u
    u.vecinos = vec_new

def maximoX(usrs):
    maximo=0
    for usr in usrs:
        if (usr.x>maximo):
            maximo=usr.x
    return maximo

def maximoY(usrs):
    maximo=0
    for usr in usrs:
        if (usr.y>maximo):
            maximo=usr.y
    return maximo
    
def algoritmo(dictUsrs, movs):
    msgs = []

    altura=maximoY(dictUsrs.values())+1
    anchura=maximoX(dictUsrs.values())+1

    rectangulo=Arbol.Rect(altura/2,anchura/2,altura,anchura)
    arbol=Arbol.QuadTree(rectangulo)

    for usr in dictUsrs.values():
        arbol.insertar(Arbol.Point(usr.x,usr.y,usr.ide))

    for mov in movs:
        # Encontrar usuario con ese id
        u = buscar(dictUsrs, mov.ide)
        
        #
        # Aqui se deberia eliminar el punto del arbol
        #

        # Mover a su nueva posición
        u.mover(mov)
        arbol.insertar(Arbol.Point(u.x,u.y,u.ide))
        # Encontrar la lista de vecinos actuales
        vecs = vecinos(u, arbol)
        # Genera mensajes y actualiza vecinos
        actualizar(u, vecs, dictUsrs, msgs)
        msgs.append("---")
    return msgs

def main():
    print("PRÁCTICA EDA 2022-23 (Referencia)")
    fich_ini = input("Fichero de estado: ")
    trozos = fich_ini.split('_')
    n = int(trozos[1])
    d = float(trozos[2])
    print(f"Parámetros: {n} {d:.1f}")
    usrs = lee_fichero_ini(fich_ini)

    dictUsr={}
    for usr in usrs:
        dictUsr.update({usr.ide:usr})

    modo = input("Modo [D]epuración o [M]edición? ").upper()
    if(modo.startswith('D')):
        # Modo Depuración
        fich_mov = input("Fichero de movimientos: ")
        if(len(fich_mov) == 0):  # Autocompletado
            fich_mov = "movs_"+'_'.join(trozos[1:])
        movs = lee_fichero_movs(fich_mov)
        print("Procesando..")
        t1 = time()
        msgs = algoritmo(dictUsr, movs)
        t2 = time()
        print(f"Tiempo: {t2-t1:.6f} seg.")
        # Se salvan los mensajes a un fichero en vez de mostrarlos por pantalla
        with open("msgs_"+'_'.join(trozos[1:]),'w') as fich:
            fich.write('\n'.join(msgs))
    else:
        # Modo Medición
        nc = int(input("Número de ciclos: "))
        movs = [Movimiento.from_usuario(usr) for usr in dictUsr]
        st = 0
        for i in range(nc):
            for mov in movs:
                mov.asigna_azar()
            t1 = time()
            algoritmo(dictUsr, movs)
            t2 = time()
            print(f"{t2-t1:.5f}")
            st += t2-t1
        print(f"Promedio: {st/nc:.5f}")


main()
