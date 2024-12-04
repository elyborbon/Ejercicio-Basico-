while True:
    vocales = "aeiou"

    cont = 0
    enunciado = str(input ("Introduce un enunciado:  "))

    contador = 0
    for letra in enunciado:
        if letra in vocales:
            contador += 1
    cont = cont +1

    print ("El numero de vocales es: ", contador)
    continue