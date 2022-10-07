from usuarios import Usuario

def pedirNumeroDensidad():
    parametros=[]
    n=input("Introduce la n: ")
    parametros.append(n)
    d=input("Introduce la densidad: ")
    parametros.append(d)

    return parametros

def imprimirId(usuarios):
    for i in range(len(usuarios)):
        print(usuarios[i].id)

def imprimirX(usuarios):
    for i in range(len(usuarios)):
        print(usuarios[i].x)

def imprimirY(usuarios):
    for i in range(len(usuarios)):
        print(usuarios[i].y)

def imprimirVecinos(usuarios):
    for i in range(len(usuarios)):
        print(usuarios[i].vecinos)

def listaVecinos(usuarios):
    vecinos=[]
    for i in range(len(usuarios)):
        vecinos.append(usuarios[i].vecinos)
    return vecinos

if __name__=="__main__":
    
    parametros=pedirNumeroDensidad()
    ficheroInicial="inicial_"+parametros[0]+"_"+parametros[1]+"_.txt"
    ficheroMovimientos="movs_"+parametros[0]+"_"+parametros[1]+"_.txt"

    usuarios=Usuario.recogerUsuarios(ficheroInicial)
    
    vecinos=[]
    vecinosCambio=[]
    for i in range(len(usuarios)):
        vecinos=Usuario.copiaVecinos(usuarios[i]) # Contiene los vecinos antes del movimiento 
        Usuario.movimientos(usuarios[i],ficheroMovimientos, usuarios)
        vecinosCambio=Usuario.copiaVecinos(usuarios[i]) # Contiene los vecinos despues del movimiento
    print(vecinosCambio)