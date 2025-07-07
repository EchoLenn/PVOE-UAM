def extraer_numeros(cadena):
    numeros = []
    palabras = cadena.split()
    for palabra in palabras:
        num = ''
        for c in palabra:
            if c.isdigit():
                num += c
            else:
                if num != '':
                    numeros.append(int(num))
                    num = ''
        if num != '':
            numeros.append(int(num))
    return numeros

def tercer_mayor(cadena):
    numeros = extraer_numeros(cadena)
    unicos = sorted(set(numeros), reverse=True)
    if len(unicos) >= 3:
        print(unicos[2])
    else:
        print("No hay suficientes numeros")

def mayor(cadena):
    numeros = extraer_numeros(cadena)
    if numeros:
        print(max(numeros))
    else:
        print("No hay numeros")

entrada = input()
mayor(entrada)
