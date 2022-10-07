from usuarios import Usuario
import time

def hallaParametros(ficheroEstado):
    ficheroEstado=ficheroEstado.split("_")
    
    print("Parametros: n = "+ficheroEstado[1]+", d = "+ ficheroEstado[2])

if __name__=="__main__":
    print("PRACTICA EDA 2022-2023")

    # Pide al usuario el nombre del fichero de estado 
    ficheroEstado=input("Fichero de estado: ")
    hallaParametros(ficheroEstado)

    modo=input("Modo [D]epuracion o [M]edicion? ")

    if (modo=="D"):
        ficheroMovimientos=input("Fichero de movimientos: ")
        print("Procesando...")

        # Lista de objeto usuario
        usuarios=Usuario.recogerUsuarios(ficheroEstado)
        
        vecinos=[]
        vecinosCambio=[]
        comienzo=time.time()

        for i in range(len(usuarios)):
            vecinos=Usuario.copiaVecinos(usuarios[i]) # Contiene los vecinos antes del movimiento 
            Usuario.movimientos(usuarios[i],ficheroMovimientos, usuarios)
            vecinosCambio=Usuario.copiaVecinos(usuarios[i]) # Contiene los vecinos despues del movimiento

            # Compruebo diferencias entre vecinos despues de cambio y vecinos
            mensajes=Usuario.generaMensajes(usuarios[i], usuarios, vecinos, vecinosCambio)
            Usuario.imprimeMensajes(mensajes)

        final=time.time()
        diferenciaTiempo=final-comienzo
        print("Tiempo: %.5f segundos" % diferenciaTiempo)

    else:
        pass

    