from usuarios import Usuario
import time

def hallaParametros(ficheroEstado):
    ficheroEstado=ficheroEstado.split("_")
    
    print("Parametros: n = "+ficheroEstado[1]+", d = "+ ficheroEstado[2])

def compruebaMensaje(mensaje,mensajesYaImpresos):
    for i in range(len(mensajesYaImpresos)):
        if (mensaje==mensajesYaImpresos[i]):
            return False
    return True

def imprimeMensajes(mensajes):
    mensajesYaImpresos=[]
    for i in range(len(mensajes)):
        if (mensajes[i]!="---"):
            if (compruebaMensaje(mensajes[i], mensajesYaImpresos)):
                print(mensajes[i])
                mensajesYaImpresos.append(mensajes[i])
        else:
            print(mensajes[i])

if __name__=="__main__":
    print("PRACTICA EDA 2022-2023")

    # Pide al usuario el nombre del fichero de estado 
    ficheroEstado=input("Fichero de estado: ")
    hallaParametros(ficheroEstado)

    # Lista de objeto usuario
    usuarios=Usuario.recogerUsuarios(ficheroEstado)

    modo=input("Modo [D]epuracion o [M]edicion? ")

    if (modo.upper()=="D"):
        ficheroMovimientos=input("Fichero de movimientos: ")
        print("Procesando...")
        
        vecinos=[]
        vecinosCambio=[]
        aux=[]
        comienzo=time.time()

        for i in range(len(usuarios)):
            vecinos=Usuario.copiaVecinos(usuarios[i]) # Contiene los vecinos antes del movimiento 
            Usuario.movimientos(usuarios[i],ficheroMovimientos, usuarios)
            vecinosCambio=Usuario.copiaVecinos(usuarios[i]) # Contiene los vecinos despues del movimiento

            # Compruebo diferencias entre vecinos despues de cambio y vecinos
            mensajes=Usuario.generaMensajes(usuarios[i], usuarios, vecinos, vecinosCambio)
            for i in range(len(mensajes)):
                aux.append(mensajes[i])

        imprimeMensajes(aux)  

        final=time.time()
        diferenciaTiempo=final-comienzo
        print("Tiempo: %.5f seg." % diferenciaTiempo)

    elif (modo.upper()=="M"):
        sumaTiempo=0
        ciclos=(int)(input("Numero de ciclos: "))
        print("Procesando...")
        
        # Repito las medidas las veces que me indica
        for iteracion in range(ciclos):
            comienzo=time.time()

            for i in range(len(usuarios)): # Recorro la lista con los usuarios
                Usuario.medicionMovimientos(usuarios[i]) # Actualizo las coordenadas x e y con un numero aleatorio entre -0.5 y 0.5 
                Usuario.cambiarVecinos(usuarios[i],usuarios) # Actualizo los vecinos segun los movimientos generados
            final=time.time()

            diferenciaTiempo=final-comienzo
            print("%.5f" % diferenciaTiempo) # Muestro el tiempo tardado
            sumaTiempo+=diferenciaTiempo 

        promedio=sumaTiempo/ciclos 
        print("Promedio: %.5f" % promedio) # Muestro el promedio de tiempo tardado
    else:
        print("OPCION ERRONEA")

    