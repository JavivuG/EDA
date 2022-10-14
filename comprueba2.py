def compruebaVecinos(usuario, vecinos):
    for i in range(len(vecinos)):
        if (usuario==vecinos[i]):
            return True # Esta en la lista de vecinos 
    return False # No esta en la lista de vecinos 

def quitarVecino(usuariosId, vecino, vecinos):
    for i in range(len(usuariosId)): 
        if (usuariosId[i]==vecino): # Selecciono el objeto usuario del vecino
            if (compruebaVecinos(usuariosId[i], vecinos)):
                vecinos=vecinos.remove(usuariosId[i])

def addVecino(usuariosId, vecino, vecinos):
    for i in range(len(usuariosId)): 
        if (usuariosId[i]==vecino): # Selecciono el objeto usuario del vecino
            if (not compruebaVecinos(usuariosId[i], vecinos)):
                vecinos=vecinos.append(usuariosId[i])

usuariosId=["PILI","PAYO","BRONCO","PAKI","BRUTUS","YUKIO","MERCHE","ORC",]
vecinos=[]
vecino="PAKI"
addVecino(usuariosId, vecino,vecinos)
print(vecinos)

for i in range(len(usuariosId)):
    if (usuariosId[i]==vecino):
        print(vecino)