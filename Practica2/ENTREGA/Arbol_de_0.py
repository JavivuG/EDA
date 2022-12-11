
"""
    Autores:
    Javier García González
    Azael Bastardo Rodríguez
    Subgrupo: k2

"""


import math



class Punto: #esta clase define los elementos que contendra el Quadtree
    def __init__(self,x,y,ide=None):
        self.x=x
        self.y=y
        self.ide=ide
        
        
    
    def distancia_a_un_punto(self, centro): #funcion que nos permite calcular la distancia entre dos puntos
        return math.sqrt((centro.x-self.x)**2 + (centro.y-self.y)**2)

class Rectangulo: #clase auxiliar que nos ayuda a definir las regiones del quadtree
    def __init__(self,centro,anchura,altura):
        self.centro = centro
        self.anchura=anchura
        self.altura=altura
        self.oeste = centro.x - anchura
        self.este = centro.x + anchura
        self.norte = centro.y - altura
        self.sur = centro.y + altura
    def contiene_punto(self,punto): #funcion que nos permite saber si un rectangulo determinado puede contener un punto
        return (self.oeste <= punto.x < self.este and
                self.norte <= punto.y < self.sur)
                
    def interseccionan(self,range): #funcion que nos permite saber si dos regiones interseccionan entre si
        return not (range.oeste > self.este or
                    range.este < self.oeste or
                    range.norte > self.sur or
                    range.sur < self.norte)
    
   
  
class Quadtree:
    def __init__(self, limite,capacidad=4):
        self.limite = limite #el rectangulo que limita al Quadtree
        self.capacidad = capacidad #Numero maximo de puntos en una region
        self.puntos = [] #Los puntos que contiene uno en concreto
        self.dividido = False #Flag que indica si tiene hijos (no,ne,se,so) o no
        
    def insertar(self,punto): #Funcion que nos permite insertar de manera recursiva un punto en su posicion correspondiente
        #Si el punto esta en el rango del Quadtree actual
        if not self.limite.contiene_punto(punto):
            return False
        #Si no tiene el maximo de puntos    
        if len(self.puntos) < self.capacidad:
            self.puntos.append(punto)
            return True
        #Si no esta dividido tendremos que dividirlo
        if not self.dividido:
            self.dividir()
            
        #Buscamos la posicon adecuada en sus hijos de manera recursiva    
        if self.no.insertar(punto):
            return True
        elif self.ne.insertar(punto):
            return True
        elif self.so.insertar(punto):
            return True
        elif self.se.insertar(punto):
            return True
        
        
        return False
        
    
        
    def buscar_en_un_radio(self,range,centro,u,radio): #Esta funcion nos permite localizar a los puntos (usuarios) que estan a menos de un radio determinado de distancia de otro punto (usuario)
        vecinos = []
       #En caso de que la zona no interseccione con la zona en la que queremos buscar no buscamos en ella para ahorra tiempo
        if not self.limite.interseccionan(range):
            return []
       #Si la zona intersecciona con la zona en la que queremos buscar analizamos los puntos para ver si estan a una distancia menor de la dada     
        for punto in self.puntos:
            if range.contiene_punto(punto) and punto.distancia_a_un_punto(centro) < radio:
                
                if(punto.ide!=None and punto.ide!=u):
                    vecinos.append(punto.ide)
                    
        #En caso de que tenga hijos buscamos recursivamente en ellos        
        if self.dividido:
            vecinos.extend(self.no.buscar_en_un_radio(range,centro,u,radio))
            vecinos.extend(self.ne.buscar_en_un_radio(range,centro,u,radio))
            vecinos.extend(self.so.buscar_en_un_radio(range,centro,u,radio)) 
            vecinos.extend(self.se.buscar_en_un_radio(range,centro,u,radio))
            
            
        return vecinos
        
    def dividir(self): #Esta funcion no permite dividir la region en 4 partes iguales. De esta manera creamos 4 nuevos Quadtrees
        centro_x = self.limite.centro.x
        centro_y = self.limite.centro.y
        nueva_anchura = self.limite.anchura / 2
        nueva_altura = self.limite.altura / 2
        #Region noroeste
        no = Rectangulo(Punto(centro_x - nueva_anchura, centro_y - nueva_altura), nueva_anchura, nueva_altura) 
        self.no = Quadtree(no)
        #Region noreste
        ne = Rectangulo(Punto(centro_x + nueva_anchura, centro_y - nueva_altura), nueva_anchura, nueva_altura)
        self.ne = Quadtree(ne)
        #Region suroeste
        so = Rectangulo(Punto(centro_x - nueva_anchura, centro_y + nueva_altura), nueva_anchura, nueva_altura)
        self.so = Quadtree(so)
        #Region sureste
        se = Rectangulo(Punto(centro_x + nueva_anchura, centro_y + nueva_altura), nueva_anchura, nueva_altura)
        self.se = Quadtree(se)
        
        self.dividido = True
        
    
        
   
            
    def eliminar_punto(self,range,centro,u): #Esta funcion nos permite eliminar los puntos del Quadtree. Para ello buscamos el punto de manera recursiva y cuando lo encontramos lo eliminamos
        
        if not self.limite.interseccionan(range):
            return False
            
        for punto in self.puntos:
            if( punto.ide==u):
                self.puntos.remove(punto)
                    
        #En caso de estar dividido buscamos el punto recursivamente en sus hijos        
        if self.dividido:
            self.no.eliminar_punto(range,centro,u)
            self.ne.eliminar_punto(range,centro,u)
            self.so.eliminar_punto(range,centro,u)
            self.se.eliminar_punto(range,centro,u)
            
        
        
        
    