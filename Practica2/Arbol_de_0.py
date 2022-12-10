
import math



class Point:
    def __init__(self,x,y,ide=None,movido=False):
        self.x=x
        self.y=y
        self.ide=ide
        self.movido=movido
        
    
    def distanceToCenter(self, center):
        return math.sqrt((center.x-self.x)**2 + (center.y-self.y)**2)

class Rectangle:
    def __init__(self,center,width,height):
        self.center = center
        self.width=width
        self.height=height
        self.west = center.x - width
        self.east = center.x + width
        self.north = center.y - height
        self.south = center.y + height
    def containsPoint(self,point):
        return (self.west <= point.x < self.east and
                self.north <= point.y < self.south)
                
    def intersects(self,range): 
        return not (range.west > self.east or
                    range.east < self.west or
                    range.north > self.south or
                    range.south < self.north)
    
   
  
class Quadtree:
    def __init__(self, boundary,capacity=4):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False
        
    def insert(self,point):
        #Si el punto esta en el rango del Quadtree actual
        if not self.boundary.containsPoint(point):
            return False
        #Si no tiene el maximo de puntos    
        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        
        if not self.divided:
            self.divide()
            
            
        if self.nw.insert(point):
            return True
        elif self.ne.insert(point):
            return True
        elif self.sw.insert(point):
            return True
        elif self.se.insert(point):
            return True
        
        
        return False
        
    
        
    def queryRadius(self,range,center,u):
        found_points = []
       
        if not self.boundary.intersects(range):
            return []
            
        for point in self.points:
            if range.containsPoint(point) and point.distanceToCenter(center) <= 2.0:
                
                if(point.ide!=None and point.ide!=u and not point.movido):
                    found_points.append(point.ide)
                    
                
        if self.divided:
            found_points.extend(self.nw.queryRadius(range,center,u))
            found_points.extend(self.ne.queryRadius(range,center,u))
            found_points.extend(self.sw.queryRadius(range,center,u)) 
            found_points.extend(self.se.queryRadius(range,center,u))
            
            
        return found_points
        
    def divide(self):
        center_x = self.boundary.center.x
        center_y = self.boundary.center.y
        new_width = self.boundary.width / 2
        new_height = self.boundary.height / 2
        
        nw = Rectangle(Point(center_x - new_width, center_y - new_height), new_width, new_height)
        self.nw = Quadtree(nw)
        
        ne = Rectangle(Point(center_x + new_width, center_y - new_height), new_width, new_height)
        self.ne = Quadtree(ne)
        
        sw = Rectangle(Point(center_x - new_width, center_y + new_height), new_width, new_height)
        self.sw = Quadtree(sw)
        
        se = Rectangle(Point(center_x + new_width, center_y + new_height), new_width, new_height)
        self.se = Quadtree(se)
        
        self.divided = True
        
    
        
   
            
    def cambiaMovido(self,punto,movido):
        found_points = []
        if not self.boundary.containsPoint(punto):
            return []
            
        for point in self.points:
            if(point.ide==punto.ide):
                if (self.boundary.containsPoint(point)):
                    point.x=movido.x
                    point.y=movido.y

                    return False
                else:
                    point.movido=True
                    return True
                
        if self.divided:
            self.nw.cambiaMovido(punto, movido)
            self.ne.cambiaMovido(punto, movido)
            self.sw.cambiaMovido(punto, movido)
            self.se.cambiaMovido(punto, movido)
            
        return found_points
        
        
    