def normalizarCodigo(codigo):
    if len(codigo) < 8:
        codigo = codigo.zfill(8)
    elif 8 <= len(codigo) < 13:
        return codigo.zfill(13)
    return codigo

def verificarIntengridad(codigo):
    digitos = list(map(int, codigo))
    cuerpo = digitos[:-1]
    digitoControl = digitos[-1]
    suma = 0
    for i in range(len(cuerpo)-1, -1, -1):
        posicion = len(cuerpo) - i
        if posicion % 2 == 1:
            suma += cuerpo[i] * 3
        else:
            suma += cuerpo[i]
    return (suma + digitoControl) % 10 == 0

def identificarPais(codigo):
    paises = {
        '0': 'Estados Unidos',
        '380': 'Bulgaria',
        '50': 'Inglaterra',
        '539': 'Irlanda',
        '560': 'Portugal',
        '70': 'Noruega',
        '759': 'Venezuela',
        '850': 'Cuba',
        '890': 'India',
    }
    for clave in sorted(paises, key=lambda x: -len(x)):
        if codigo.startswith(clave):
            return paises[clave]
    return 'Desconocido'

def main():
    codigo = input("Codigo de barras a verificar: ").strip()
    if not codigo.isdigit():
        print("Codigo invalido. Solo se permiten digitos numericos.")
        return
    codigo = normalizarCodigo(codigo)
    if verificarIntengridad(codigo):
        if len(codigo) == 13:
            pais = identificarPais(codigo)
            print(f"Codigo de barras valido del pais {pais}")
        else:
            print("Codigo de barras valido")
    else:
        print("Codigo de barras NO valido")

if __name__ == "__main__":
    main()
