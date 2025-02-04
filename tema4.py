#ejercicios 3, 5 y 6

def ejercicio_4_3(clave):
    clave_impar = ""
    clave_par = ""
    for i in range(len(clave)):
        if i % 2 != 0:
            clave_impar += clave[i]
        else:
            clave_par += clave[i]
    return clave_impar, clave_par


def ejercicio_4_5_ciclos(cadena, numero_caracteres):
    lista_palabras_caracteres = []
    for palabra in cadena.split():
        if len(palabra) >= numero_caracteres:
            lista_palabras_caracteres.append(palabra)
    return " ".join(lista_palabras_caracteres)

def ejercicio_4_5_comprension(cadena, numero_caracteres):
    return " ".join([palabra for palabra in cadena.split() if len(palabra) >= numero_caracteres])

def ejercicio_4_5_filtro(cadena, numero_caracteres):
    return " ".join(cadena.split().filter(lambda palabra: len(palabra) >= numero_caracteres))

def ejercicio_4_6(cadena, posicion, numero_letras):
    return cadena[posicion:posicion + numero_letras + 1]

print(ejercicio_4_6("El nnúmero de teléfono es 4356-7890", 25, 9))