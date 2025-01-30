from random import *


def ejercicio_2_2_a(numero_elementos):
    lista_elementos = []
    for _ in range(numero_elementos):
        lista_elementos.append(randint(1, 100))
    return lista_elementos

def ejercicio_2_2_b(lista_elementos):
    for i in range(len(lista_elementos)):
        if lista_elementos.count(lista_elementos[i]) > 1:
            return True
    return False

def ejercicio_2_2_c(lista_elementos):
    nueva_lista = []
    for i in range(len(lista_elementos)):
        if lista_elementos[i] not in nueva_lista:
            nueva_lista.append(lista_elementos[i])
    return nueva_lista


def ejercicio_2_4(lista_elementos_1, lista_elementos_2):
    print(lista_elementos_1)
    lista_a_eliminar = []
    for i in range(len(lista_elementos_2)):
        if lista_elementos_2[i] in lista_elementos_1:
            lista_a_eliminar.append(lista_elementos_2[i])
            while lista_elementos_2[i] in lista_elementos_1:
                lista_elementos_1.remove(lista_elementos_2[i])
    print(lista_a_eliminar)
    print(lista_elementos_1)