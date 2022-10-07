import math

class Usuario():
    def __init__(self,id,x,y,grupo,vecinos):
            self.id=id
            self.x=x
            self.y=y
            self.grupo=grupo
            self.vecinos=vecinos

    def recogerUsuarios(ficheroInicial): # Extrae los datos de los usuarios en el punto inicial
        fichero = open("./ficheros/"+ficheroInicial,'r')
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

    # Actualiza la posicion x e y de los usuarios segun el fichero de movimientos
    def movimientos(self,ficheroMovimientos,usuarios): 
        fichero = open("./ficheros/"+ficheroMovimientos,'r')
        lineas = fichero.readlines()

        datos=[]
        for i in range(len(lineas)):
            datos.append(lineas[i].split())

        for i in range(len(datos)):
            if (self.id==datos[i][0]):
                self.x=datos[i][1] # Actualizo la posicion x
                self.y=datos[i][2] # Actualizo la posicion y
        self.cambiarVecinos(usuarios)

    def cambiarVecinos(self,usuarios): # Cambiar vecinos despues de movimientos
        vecinos=[]
        for i in range(len(usuarios)):
            if (self.id!=usuarios[i].id):
                distancia=math.sqrt(((float)(self.x)-(float)(usuarios[i].x))**2+((float)(self.y)-(float)(usuarios[i].y))**2)
                if (distancia<=2.0):
                    vecinos.append(usuarios[i].id)
                    
        self.vecinos=vecinos

    # Realiza una copia de los vecinos de un usuario
    def copiaVecinos(self):
        copiaVecinos=[]
        for i in range(len(self.vecinos)):
            copiaVecinos.append(self.vecinos[i])
        return copiaVecinos

    def generaMensajes(self,usuarios,vecinos, vecinosCambio):
        mensajes=[]
        for i in range(len(vecinos)):
            if(vecinos[i] not in vecinosCambio):
                mensajes.append(self.id+"-"+vecinos[i])
                mensajes.append(vecinos[i]+"-"+self.id)
            mensajes.append("---")

        for i in range(len(vecinosCambio)):
            if (vecinosCambio[i] not in vecinos):
                if (self.compruebaGrupo(usuarios, vecinosCambio[i])):
                    mensajes.append(self.id+"+="+vecinosCambio[i])
                    mensajes.append(vecinosCambio[i]+"+="+self.id)
                else:
                    mensajes.append(self.id+"+/"+vecinosCambio[i])
                    mensajes.append(vecinosCambio[i]+"+/"+self.id)
            mensajes.append("---")
        
        self.vecinos=vecinosCambio
        return mensajes

    def compruebaGrupo(self, usuarios,vecino): #Comprueba si son del mismo grupo
        for i in range(len(usuarios)):
            if (usuarios[i].id==vecino):
                if (usuarios[i].grupo==self.grupo):
                    return True
                else:
                    return False
    
    def imprimeMensajes(mensajes):
        for i in range(len(mensajes)):
            print(mensajes[i])


