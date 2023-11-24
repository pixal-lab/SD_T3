import argparse, re
import json

def buscador(archivo, palabra):
    with open(archivo, 'r') as file:
        lineas = file.readlines()

    inicio = 0
    fin = len(lineas) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        linea_actual = lineas[medio]
        datos = linea_actual.split("\t")
        if datos[0] == palabra:
            pares = re.findall(r'\((\d+), (\d+)\)', datos[1])
            # Convertir los pares de cadenas a pares de enteros
            pares = [(int(x), int(y)) for x, y in pares]
            # Ordenar el arreglo según el segundo valor de cada par, de mayor a menor
            arr = sorted(pares, key=lambda x: x[1], reverse=True)
            imprimir(palabra, arr)
            return None
        elif datos[0] < palabra:
            inicio = medio + 1
        else:
            fin = medio - 1
    print(f"Error: La palabra '{palabra}' no se encontró en el archivo.")

def imprimir(palabra, arr):
    # Selecciona solo los primeros 5 elementos de la lista 'datos'
    arr = arr[:5]

    # Crea una lista de diccionarios con las claves "Documento" y "Frecuencia"
    resultado = [{"Documento": doc, "Frecuencia": freq} for doc, freq in arr]

    # Crea el diccionario final con la palabra y la lista de diccionarios
    resultado_final = {palabra: resultado}

    # Convierte el diccionario a formato JSON
    json_resultado = json.dumps(resultado_final, indent=4)

    # Imprime el resultado
    print(json_resultado)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('palabra', type=str, help='Palabra a buscar')
    args = parser.parse_args()

    path = 'outhadoop/part-00000'
    word = args.palabra
    buscador(path, word)
