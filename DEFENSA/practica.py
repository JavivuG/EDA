# Trabajo realizado por: 
# Javier García González
# Azael Bastardo Rodríguez
# Grupo de Laboratorio: K2
# Este es la parte ejecutable del programa, el fichero usuarios.py contiene la clase usuario y los metodos relacionados
# IMPORTANTE: Se debe introducir el nombre completo de los ficheros cuando se solicitan, ejemplo: "inicial_10_0.3_.txt"
from usuarios import Usuario
import time


def hallaParametros(ficheroEstado): # Hallo los parametros a partir del fichero de Estado introducido
    ficheroEstado=ficheroEstado.split("_")
    
    print("Parametros: n = "+ficheroEstado[1]+", d = "+ ficheroEstado[2])

def imprimeMensajes(mensajes): # Imrpime por pantalla los mensajes generados
    mensajesYaImpresos=[]
    for i in range(len(mensajes)):
        if (mensajes[i]!="---"):
            if (compruebaMensaje(mensajes[i], mensajesYaImpresos)): # Evito que se repitan los mismos mensajes
                print(mensajes[i])
                mensajesYaImpresos.append(mensajes[i])
        else:
            print(mensajes[i])

def compruebaMensaje(mensaje,mensajesYaImpresos): # Compruebo que le mensaje se halla imprimido o no
    for i in range(len(mensajesYaImpresos)):
        if (mensaje==mensajesYaImpresos[i]):
            return False
    return True


def usuariosFicheroMoviemientos(ficheroMovimientos): # Devuelvo la lista de nombres de usuarios ordenados segun el fichero de movimientos
    usuarios=[]
    fichero = open(ficheroMovimientos,'r')
    lineas = fichero.readlines()
    datos=[]
    for i in range(len(lineas)):
        datos.append(lineas[i].split())
        usuarios.append(datos[i][0])
    return usuarios

def ordenarPorMovimientos(usuarios, ficheroMovimientos): # Ordeno la lista de objetos usuario por orden de apariencia en el fichero de movimientos
    usuariosPorMovimientos=usuariosFicheroMoviemientos(ficheroMovimientos) # Lista de nombres de usuario
    usuariosOrdenados=[] # Lista de objetos usuario

    for i in range(len(usuariosPorMovimientos)):
        for j in range(len(usuarios)):
            if (usuariosPorMovimientos[i]==usuarios[j].id):
                usuariosOrdenados.append(usuarios[j])
    return usuariosOrdenados

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
        todosMensajes=[]
        comienzo=time.time()

        usuarios=ordenarPorMovimientos(usuarios, ficheroMovimientos)
        
        for i in range(len(usuarios)):
            vecinos=usuarios[i].vecinos # Contiene los vecinos antes del movimiento 
            Usuario.movimientos(usuarios[i],ficheroMovimientos, usuarios)
            vecinosCambio=usuarios[i].vecinos # Contiene los vecinos despues del movimiento
    
            # Compruebo diferencias entre vecinos despues de cambio y vecinos
            mensajes=Usuario.generaMensajes(usuarios[i], usuarios, vecinos, vecinosCambio)
            
            for j in range(len(mensajes)):
                todosMensajes.append(mensajes[j])

        imprimeMensajes(todosMensajes)  

        final=time.time()
        diferenciaTiempo=final-comienzo
        print("Tiempo: %.5f seg." % diferenciaTiempo)

    elif (modo.upper()=="M"):
        sumaTiempo=0
        ciclos=(int)(input("Numero de ciclos: "))
        print("Procesando...")
        
        # Repito las medidas las veces que me indica
        for iteracion in range(ciclos+1):
            comienzo=time.time()

            for i in range(len(usuarios)): # Recorro la lista con los usuarios
                Usuario.medicionMovimientos(usuarios[i]) # Actualizo las coordenadas x e y con un numero aleatorio entre -0.5 y 0.5 
                Usuario.cambiarVecinos(usuarios[i],usuarios) # Actualizo los vecinos segun los movimientos generados
            final=time.time()

            if (iteracion>0):
                diferenciaTiempo=final-comienzo
                print("%.5f" % diferenciaTiempo) # Muestro el tiempo tardado
                sumaTiempo+=diferenciaTiempo 

        promedio=sumaTiempo/(ciclos)
        print("Promedio: %.5f" % promedio) # Muestro el promedio de tiempo tardado
    else:
        print("OPCION ERRONEA")
