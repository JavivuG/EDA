import math

class Usuario():
    def __init__(self,id,x,y,grupo,vecinos):
            self.id=id
            self.x=x
            self.y=y
            self.grupo=grupo
            self.vecinos=vecinos

    def recogerUsuarios(ficheroInicial): # Extrae los datos de los usuarios en el punto inicial
        fichero = open(ficheroInicial,'r')
        lineas = fichero.readlines()
        datos=[]
        for i in range(len(lineas)):
            datos.append(lineas[i].split())
        usuarios=[Usuario]*(len(lineas)) # Creo tantos objetos como lineas tenga el fichero

        Vecinos=[] 
        for i in range(len(usuarios)): # Extraer los vecinos de cada uno de ellos
            contador=len(datos[i])
            vecinosUsuario=[]
            for j in range(4,contador):
                vecinosUsuario.append(datos[i][j])
            Vecinos.append(vecinosUsuario)
            usuarios[i]=Usuario(datos[i][0],datos[i][1],datos[i][2],datos[i][3],Vecinos[i])
                
        return usuarios

    def movimientos(self,ficheroMovimientos): # Funciona
        fichero = open(ficheroMovimientos,'r')
        lineas = fichero.readlines()

        datos=[]
        for i in range(len(lineas)):
            datos.append(lineas[i].split())

        for i in range(len(datos)):
            if (self.id==datos[i][0]):
                self.x=datos[i][1] # Actualizo la posicion x
                self.y=datos[i][2] # Actualizo la posicion y


    # Esto todavia no esta implementado pero deberia funcionar
    def recogerVecinos(self,usuarios): # Recoger vecinos despues de movimientos
        vecinos=[]
        for i in range(len(usuarios)):
            if (self.id!=usuarios[i].id):
                distancia=math.sqrt(((float)(self.x)-(float)(usuarios[i].x))**2+((float)(self.y)-(float)(usuarios[i].y))**2)
                if (distancia<=2.0):
                    vecinos.append(usuarios[i].id)
                    
        self.vecinos=vecinos


