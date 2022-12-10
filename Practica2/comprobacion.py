def lee_fichero_movs(fichOriginal, fich):
    contador=0
    with open(fich, 'r') as fich:
        modificado=fich.readlines()
    with open(fichOriginal, "r") as fichero:
        original=fichero.readlines()
    for i in range(len(modificado)):
        
        if (modificado[i] not in original):
            print(i+1)
            print(modificado[i])
            break
        contador=i
    print(contador)

lee_fichero_movs("ficheroOriginal.txt","msgs_14000_1.0_.txt")