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


def ejercicio_4_9(cadena):
    return " ".join(sorted([palabra.strip() for palabra in cadena.split()],
                           key=lambda letra: sum(list(map(lambda y: 1 if y.isalnum() else 0, letra)))))


def ejercicio_4_14():
    lista_dominios = []
    email = str(input("Ingrese su correo, o una cadena vacía para terminar: "))
    while email != "":

        if email.count('@') != 1:
            print("El correo debe tener un único carácter arroba")
            email = str(input("Ingrese su correo, o una cadena vacía para terminar: "))
            continue

        partes_email = email.split('@')

        if not partes_email[0].isalnum():
            print("El nombre de usuario debe ser alfanumérico")
            email = str(input("Ingrese su correo, o una cadena vacía para terminar: "))
            continue

        partes_dominio = partes_email[1].split('.', maxsplit=1)

        if partes_dominio[1] not in ["com", "com.ar"]:
            print("El dominio del correo electrónico debe ser solo .com o .com.ar")
            email = str(input("Ingrese su correo, o una cadena vacía para terminar: "))
            continue

        if partes_dominio[0] not in lista_dominios:
            lista_dominios.append(partes_dominio[0].lower())
        email = str(input("Ingrese su correo, o una cadena vacía para terminar: "))
    return sorted(lista_dominios)
