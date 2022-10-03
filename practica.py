from usuarios import Usuario

if __name__=="__main__":
    ficheroInicial="inicial_20_0.1_.txt"
    ficheroMovimientos="movs_20_0.1_.txt"
    usuarios=Usuario.recogerUsuarios(ficheroInicial)
    for instance in usuarios[0].all:
        print(instance.x)
    print()
    movimientos=Usuario.movimientos(usuarios[0],ficheroMovimientos)
    for instance in usuarios[0].all:
        print(instance.x)
