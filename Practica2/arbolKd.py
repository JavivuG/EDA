class Nodo:
    izq , der, dato = None, None, 0
    
    def __init__(self, dato):
        # crea un Nodo
        self.izq = None
        self.der = None
        self.dato = dato

def arbolkd(listaCoordenadas, depth=0):
    if not listaCoordenadas:
        return

    # Select eje based on depth so that eje cycles through all valid values
    k = len(listaCoordenadas[0]) # assumes all points have the same dimension
    eje = depth % k

    # Sort point list and choose median as pivot element
    listaCoordenadas.sort(key=lambda x:x[eje])
    median = len(listaCoordenadas)/2 # choose median

    # Create Nodo and construct subtrees
    Nodo = Nodo()
    Nodo.location = listaCoordenadas[median]
    Nodo.hijaIzq = arbolkd(listaCoordenadas[0:median], depth+1)
    Nodo.hijoDer = arbolkd(listaCoordenadas[median+1:], depth+1)
    return Nodo