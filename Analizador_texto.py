texto = input("Ingrese un texto: ") ##aqui ingreso el texto
texto = texto.lower() ## el texto lo convierto a minúsculas para su uso correcto
##print(texto)
letras = input("Ingresa tres letras: ") ##ingreso las tres letras
letras = letras.lower() ## las letras también las convierto a minúsculas para su uso correcto.
lista = list(letras)##las paso a una lista
##print(lista)

####Aquí guardo cada letra de la lista en una variable
l1 = lista[0]
l2 = lista[1]
l3 = lista[2]

##aquí se guarda la cantidad de veces que está cada letra
c1=texto.count(l1)
c2=texto.count(l2)
c3=texto.count(l3)
##imprimo las veces que se encuentra cada letra en el texto (parte 1)
print("Parte 1:")
print(f"Las veces que aparece {l1} son: {c1}\nLas veces que aparece {l2} son: {c2}\nLas veces que aparece {l3} son: {c3}\n")

#Vamos a desplegar la cantidad de palabras que hay (parte 2)
list_texto = len(texto.split())
##print(list_texto)
print("Parte 2: ") ##imprime la cantidad de palabras que hay en el texto
print(f"La cantidad de palabras que posee son: {list_texto}\n")
print("Parte 3: ")#imprime la primera y ultima letra que hay en el texto
prim_letra = texto[0]
ult_letra = texto[-1]
print(f"La primer letra del texto ingresdo es: {prim_letra}\nLa últma letra del texto ingresado es: {ult_letra}\n")
print("Parte 4: ") #Coloca en reversa las palabras del texto
list_texto_2 =texto.split()##convierto el texto en lista
##print(list_texto_2)
list_texto_2.reverse()##aquí reverso la lista
##print(list_texto_2)
unir_nuevo = " ".join(list_texto_2)
print(unir_nuevo)
print("\nParte 5: ")#Verifica si la palabra Python está en el texto
buscar_py = 'python' in texto
dic = {True: "si", False: "no"}
print(f"La palabra 'python' {dic[buscar_py]} se encuentra en el texto ingresado")
##aquí, relaciona la comparación en buscar_ý con el diccionario creado.
