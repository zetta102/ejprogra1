def ejercicio_2_11():
    lista_pacientes = []
    num_afiliado = int(input("Ingrese el nùmero de afiliado de 4 dìgitos: "))
    while num_afiliado != -1:
        tipo_de_turno = int(input("Ingrese el tipo de consulta por la que viene. 0 para urgencia o 1 para turno: "))
        lista_pacientes.append([num_afiliado, tipo_de_turno])
        num_afiliado = int(input("Ingrese el nùmero de afiliado de 4 digitos: "))

    pacientes_por_urgencias = [fila[0] for fila in lista_pacientes if fila[1] == 0]
    print(f"Pacientes atendidos por urgencias: {pacientes_por_urgencias}")
    pacientes_por_turnos = [fila[0] for fila in lista_pacientes if fila[1] -- 1]
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
            print(f"{columna:3d}", end=" ")
        print()


def ejercicio_3_2_f(n):
    matriz = [[0 for f in range(n)] for c in range(n)]
    longitud_fila = len(matriz[0]) - 1
    contador_posicion= 1
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if c >= longitud_fila:
                matriz[f][c] = contador_posicion
                contador_posicion += 1
            else:
                matriz[f][c] = 0
        longitud_fila -= 1
    imprimirMatriz(matriz)


ejercicio_3_2_f(4)