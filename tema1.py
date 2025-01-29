def es_bisiesto(ano):
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0


def es_primo(numero):
    return not (numero % 2 == 0 or numero % 3 == 0)


def ejercicio1_2(dia, mes, ano):
    if not (1 <= dia <= 31):
        return False
    if not (1 <= mes <= 12):
        return False
    if not (1 <= ano <= 9999):
        return False

    match dia:
        case 31 if mes not in [1, 3, 5, 7, 8, 10, 12]:
            return False
        case 30 if mes not in [4, 6, 9, 11]:
            return False
        case 29 if mes == 2 and not es_bisiesto(ano):
            return False
        case 28 if mes == 2 and es_bisiesto(ano):
            return False
        case _:
            return True


def ejercicio1_7_diasiguiente(dia, mes, ano):
    """Por propósitos de brevedad de código, se asume y espera que todos los parámetros sean positivos"""
    match dia:
        case 31 if mes in [1, 3, 5, 7, 8, 10]:
            dia = 1
            mes += 1
        case 31 if mes == 12:
            dia = 1
            mes = 1
            ano += 1
        case 30 if mes in [4, 6, 9, 11]:
            dia = 1
            mes += 1
        case 29 if mes == 2 and es_bisiesto(ano):
            dia = 1
            mes += 1
        case 28 if mes == 2 and not es_bisiesto(ano):
            dia = 1
            mes += 1
        case _:
            dia += 1
    return dia, mes, ano


def ejercicio1_7_a(dia, mes, ano, dias_extra):
    """Por propósitos de brevedad de código, se asume y espera que el valor dias_extra sea un valor positivo"""
    for _ in range(dias_extra):
        dia, mes, ano = ejercicio1_7_diasiguiente(dia, mes, ano)
    return dia, mes, ano


def ejercicio1_7_b(dia1, mes1, ano1, dia2, mes2, ano2):
    """Por propósitos de brevedad de código, se asume y espera que la primera fecha sea más antigua que la segunda"""
    contador_dias = 0
    while dia1 != dia2 or mes1 != mes2 or ano1 != ano2:
        dia1, mes1, ano1 = ejercicio1_7_diasiguiente(dia1, mes1, ano1)
        contador_dias += 1
    return contador_dias


def ejercicio1_8_diadelasemana(dia, mes, ano):
    if mes < 3:
        mes += 10
        ano -= 1
    else:
        mes -= 2
    siglo = ano // 100
    ano2 = ano % 100
    diasem = (((26 * mes - 2) // 10) + dia + ano2 + (ano2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    if diasem < 0:
        diasem = diasem + 7
    return diasem


def ejercicio1_8(mes, ano):
    match mes:
        case [1, 3, 5, 7, 8, 10, 12]:
            cant_dias = 31
        case [4, 6, 9, 11]:
            cant_dias = 30
        case 2 if es_bisiesto(ano):
            cant_dias = 29
        case 2 if not es_bisiesto(ano):
            cant_dias = 28
        case _:
            cant_dias = 30

    for i in range(cant_dias):
        if i % 7 == 0:
            print()
        print(ejercicio1_8_diadelasemana(i, mes, ano), end=" ")