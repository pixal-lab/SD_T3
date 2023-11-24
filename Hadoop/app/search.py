def buscar_palabra_binario(archivo, palabra):
    with open(archivo, 'r') as file:
        lineas = file.readlines()

    inicio = 0
    fin = len(lineas) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        linea_actual = lineas[medio]
        datos = linea_actual.split("\t")
        print(datos)
        if datos[0] == palabra:
            return datos
        elif datos[0] < palabra:
            inicio = medio + 1
        else:
            fin = medio - 1

    print(f"Error: La palabra '{palabra}' no se encontró en el archivo.")
    return None

# Ejemplo de uso
archivo_datos = '/home/pixal/U archivos/SD/T3/Ayudantia-2023-2S/Ayu3/Hadoop/examples/outhadoop/part-00000'
palabra_buscada = 'tesla'

resultados = buscar_palabra_binario(archivo_datos, palabra_buscada)

if resultados:
    for resultado in resultados:
        print(f'Archivo: {resultado[0]}, Frecuencia: {resultado[1]}')
else:
    print(f'La palabra "{palabra_buscada}" no se encontró en el archivo.')
