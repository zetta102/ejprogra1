import random
import string


def ejercicio_2_11():
    lista_pacientes = []
    num_afiliado = int(input("Ingrese el nùmero de afiliado de 4 dìgitos: "))
    while num_afiliado != -1:
        tipo_de_turno = int(input("Ingrese el tipo de consulta por la que viene. 0 para urgencia o 1 para turno: "))
        lista_pacientes.append([num_afiliado, tipo_de_turno])
        num_afiliado = int(input("Ingrese el nùmero de afiliado de 4 digitos: "))

    pacientes_por_urgencias = [fila[0] for fila in lista_pacientes if fila[1] == 0]
    print(f"Pacientes atendidos por urgencias: {pacientes_por_urgencias}")
    pacientes_por_turnos = [fila[0] for fila in lista_pacientes if fila[1] - - 1]
    print(f"Pacientes atendidos por turnos: {pacientes_por_turnos}")

    num_afiliado = int(input("Ingrese el numero de afiliado de 4 digitos cuya informaciòn desea buscar: "))
    while num_afiliado != -1:
        num_afiliado_urgencias = lista_pacientes.count([num_afiliado, 0])
        print(f"El nùmero de afiliado {num_afiliado} fue atendido {num_afiliado_urgencias} veces por urgencias")
        num_afiliado_turnos = lista_pacientes.count([num_afiliado, 1])
        print(f"El nùmero de afiliado {num_afiliado} fue atendido {num_afiliado_turnos} veces por turnos")
        num_afiliado = int(input("Ingrese el numero de afiliado de 4 digitos cuya informaciòn desea buscar: "))


def imprimirMatriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(f"{str(columna)}", end=" ")
        print()


def cargar_matriz_cuadrada(n):
    return [[0 for f in range(n)] for c in range(n)]


def cargar_butacas(n):
    return [[[f"{c}{f + 1}", False] for f in range(n)] for c in list(string.ascii_uppercase[:n])]


def ejercicio_3_2_f(n):
    matriz = cargar_matriz_cuadrada(n)
    longitud_fila = len(matriz[0]) - 1
    contador_posicion = 1
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if c >= longitud_fila:
                matriz[f][c] = contador_posicion
                contador_posicion += 1
            else:
                matriz[f][c] = 0
        longitud_fila -= 1
    imprimirMatriz(matriz)


def reservar(matriz, butaca):
    for fila in matriz:
        for columna in fila:
            if columna.count([butaca, False]) == 0:
                columna[1] = True
                return True
    return False


def butacas_libres(matriz):
    contador_butacas = 0
    for fila in matriz:
        for columna in fila:
            for butaca in columna:
                if not butaca[1]:
                    contador_butacas += 1
    return contador_butacas


def cargar_sala(matriz):
    for fila in matriz:
        for columna in fila:
            columna[1] = random.choice([True, False])


def butacas_contiguas_libres(matriz):
    contador_butacas = -1
    contador_libre_inicial = ""
    for fila in matriz:
        contador_butacas_aux = -1
        contador_libre_aux = ""
        for i in range(len(fila)):
            if not fila[i][1]:
                contador_butacas_aux += 1
                if contador_libre_aux == "":
                    contador_libre_aux = fila[i][0]
        if contador_butacas_aux > contador_butacas:
            contador_butacas = contador_butacas_aux
            contador_libre_inicial = contador_libre_aux
    return contador_libre_inicial


def ejercicio_3_5(n):
    matriz = cargar_butacas(n)
    imprimirMatriz(matriz)
    cargar_sala(matriz)
    butaca = input("Introduzca la butaca a buscar, en el formato numero de fila + letra. P. ej. C2: ")
    resultado_reseva = reservar(matriz, butaca)
    print(f"Se ha reservado exitosamente la butaca {butaca}" if resultado_reseva else f"No se pudo resevar la butaca {butaca}")
    butaca_libre = butacas_contiguas_libres(matriz)
    print(f"La mayor cantidad de butacas libres se encuentran a partir de la butaca: {butaca_libre}")
    imprimirMatriz(matriz)
