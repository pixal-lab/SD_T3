import argparse



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
            pares = [list(map(int, par.strip('()').split(','))) for par in datos[1].split()]

            # Paso 3: Ordenar la lista de listas según el segundo valor de cada par
            arr_ordenado = sorted(pares, key=lambda x: x[1], reverse=True)
            print(arr_ordenado)
            return datos
        elif datos[0] < palabra:
            inicio = medio + 1
        else:
            fin = medio - 1

    print(f"Error: La palabra '{palabra}' no se encontró en el archivo.")
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('palabra', type=str, help='Palabra a buscar')
    args = parser.parse_args()

    path = 'outhadoop/part-00000'
    word = args.palabra
    buscador(path, word)