def hallaParametros(ficheroEstado):
    ficheroEstado=ficheroEstado.split("_")
    return ficheroEstado

print(hallaParametros("inicial_20_0.1_.txt"))