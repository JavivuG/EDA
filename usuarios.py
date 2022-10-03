class Usuario:
    def __init__(self,id,x,y,grupo,vecinos):
            self.id=id
            self.x=x
            self.y=y
            self.grupo=grupo
            self.vecinos=vecinos

    def recogerUsuarios(nombreFichero):
        ficheroUsuarios = open(nombreFichero,'r')
        lineas = ficheroUsuarios.readlines()
        datos=[]
        for i in range(len(lineas)):
            datos.append(lineas[i].split())
        usuarios=[Usuario]*(len(lineas))

        Vecinos=[] 
        for i in range(len(usuarios)): # Extraer los vecinos de cada uno de ellos
            contador=len(datos[i])
            vecinosUsuario=[]
            for j in range(4,contador):
                vecinosUsuario.append(datos[i][j])
            Vecinos.append(vecinosUsuario)
            usuarios[i]=Usuario(datos[i][0],datos[i][1],datos[i][2],datos[i][3],Vecinos[i])
                
        return usuarios
        
    # Esto todavia no esta implementado pero deberia funcionar
    """def recogerVecinos(nombreFichero): # Recoger vecinos despues de movimientos
        usuarios=recogerUsuarios(nombreFichero)
        vecinos=[]
        for i in range(len(usuarios)):
            for j in range(len(usuarios)):
                if (usuarios[i]!=usuarios[j]):
                    distancia=Math.sqrt((usuarios[i].x-usuario[j].x)**2+(usuarios[i].y-usuario[j].y)**2)
                    if distancia=<2:
                        vecinos.append(usuario[j])
        return vecinos"""


