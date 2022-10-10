from comprueba2 import Usuario

def hallaParametros(ficheroEstado):
    ficheroEstado=ficheroEstado.split("_")
    
    print("Parametros: n = "+ficheroEstado[1]+", d = "+ ficheroEstado[2])

def imprimeMensajes(mensajes):
    for i in range(len(mensajes)):
        print(mensajes[i])

if __name__=="__main__":
    print("PRACTICA EDA 2022-2023")

    # Pide al usuario el nombre del fichero de estado 
    ficheroEstado="inicial_10_0.3_.txt"
    hallaParametros(ficheroEstado)

    # Lista de objeto usuario
    usuarios=Usuario.recogerUsuarios(ficheroEstado)

    modo=input("Modo [D]epuracion o [M]edicion? ")

    if (modo.upper()=="D"):
        ficheroMovimientos="movs_10_0.3_.txt"
        print("Procesando...")
        
        vecinos=[]
        vecinosCambio=[]

        for i in range(len(usuarios)):
            vecinos=Usuario.copiaVecinos(usuarios[i]) # Contiene los vecinos antes del movimiento 
            Usuario.movimientos(usuarios[i],ficheroMovimientos, usuarios)
            vecinosCambio=Usuario.copiaVecinos(usuarios[i]) # Contiene los vecinos despues del movimiento

            
            print(vecinos)
            print(vecinosCambio)
            print()
