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
            print(datos)
            return datos
        elif datos[0] < palabra:
            inicio = medio + 1
        else:
            fin = medio - 1

    print(f"Error: La palabra '{palabra}' no se encontró en el archivo.")
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('Palabra', type=str, help='Palabra a buscar')
    args = parser.parse_args()

    path = 'outhadoop/part-00000'
    word = args.palabra
    buscador(path, word)