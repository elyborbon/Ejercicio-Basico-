veces =  int (input ("Cuantos numeros quieres ingresar?  "))

cont = 0
cont1 = 0
for i in range(veces) :
    
    numero= int (input("Ingrese un numero:  "))

    if numero % 2 == 0:
        cont += 1
    else:
        cont1 += 1 
print ("La cantidad de numeros pares:  ", cont)
print ("La suma total de numeros impares es: ", cont1)
