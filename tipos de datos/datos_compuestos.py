lista = ["Mauro Harretche" , "Corredor" , True, 1.73]
tupla = ("Mauro Harretche" , "Corredor" , True, 1.73)


#esto es válido
lista[3] = "maquinola"

#esto no es válido
#tupla[3] = "maquinola"

#creando un conjunto (set) (no se accede a los elementos por índice, no almacena datos duplicados)
conjunto = {"Mauro Harretche" , "Corredor" , True, 1.73}

#print(conjunto[3]) -> no puede acceder al elemento por su indice

#creando un diccionario (dict) la estructura es key : value y separamos por comas
diccionario = {
    'nombre' : "Mauro Harretche",
    'lenguaje' : "Python",
    'altura' : 1.73,
    'esta_emocionado' : True,
    'dato_duplicado' : "Python"
}

print(diccionario['nombre'])