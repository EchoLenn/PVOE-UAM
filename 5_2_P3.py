import random  # Importa el módulo para generar números aleatorios
import math    # Importa el módulo matemático para redondear al siguiente entero multiplo de 100

# Lista de inmuebles
listaInmuebles = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

# Función que calcula el precio y genera un ID para cada inmueble
def calcular_precios(lista):
    lista_calculada = []  # Lista vacía para almacenar inmuebles con precio e ID
    for inmueble in lista: 
        antiguedad = 2025 - inmueble['año']  # Calcula antigüedad del inmueble
        # Calcula el valor base según metros, habitaciones y si tiene garaje por formula dada
        base = (inmueble['metros'] * 1000) + (inmueble['habitaciones'] * 5000) + ((15000 if inmueble['garaje'] else 0))
        
        if inmueble['zona'] == 'A':  # Si la zona es A, precio base con descuento por antigüedad
            precio = base * (1 - antiguedad / 100)
        else:  # Si la zona es B, precio base con descuento y multiplicado por 1.5
            precio = base * (1 - antiguedad / 100) * 1.5
        
        precio = math.ceil(precio / 1000) * 1000  # Redondea precio
        
        # Genera un ID único para el inmueble, combinando zona y número aleatorio
        id_inmueble = inmueble['zona'] + str(random.randint(100, 999))
        
        # Agrega los nuevos campos al diccionario del inmueble
        inmueble['id'] = id_inmueble
        inmueble['precio'] = precio
        inmueble['antiguedad'] = antiguedad
        
        # Añade el inmueble modificado a la lista calculada
        lista_calculada.append(inmueble)
    return lista_calculada  # Devuelve la lista con inmuebles y sus precios e IDs

# Buscar y muestra inmuebles que caben dentro del presupuesto
def busqueda_inmueble(lista, presupuesto):
    # Filtra los inmuebles cuyo precio sea menor o igual al presupuesto
    filtrados = [i for i in lista if i['precio'] <= presupuesto]
    print(f"\nLista de inmuebles dentro del presupuesto con ${presupuesto}")
    print("Id Inmueble\tAño\tMetros\tHabitaciones\tGaraje\tPrecio")
    
    # Imprime en forma de tabla los inmuebles filtrados
    for i in filtrados:
        print(f"{i['id']}\t\t{i['año']}\t{i['metros']}\t{i['habitaciones']}\t\t{i['garaje']}\t${i['precio']}")
    
    # Si no hay ningún inmueble dentro del presupuesto, muestra mensaje
    if not filtrados:
        print("No se encontraron inmuebles dentro del presupuesto.")

# Ejecucion del Programa
def main():
    inmuebles = listaInmuebles  # Usa la lista de inmuebles
    lista_con_precios = calcular_precios(inmuebles)  # Calcula precios y genera IDs
    presupuesto = float(input("Ingresa el presupuesto para el inmueble: $"))  # Pide presupuesto al usuario
    busqueda_inmueble(lista_con_precios, presupuesto)  # Muestra inmuebles dentro del presupuesto

if __name__ == '__main__':
    main()

