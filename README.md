# Implementacion Hadoop
## Uso

Creacion y levantamiento de Hadoop
```sh
git clone https://github.com/pixal-lab/SD_T3
cd SD_T3
docker compose up -d
```

Extraccion de los documentos de wikipedia:
```sh
cd Hadoop/app/
python3 wp.py
```

Se accede al contenedor que contiene el servicio de hadoop:
```sh
docker exec -it hadoop bash
```

Creación de directorios para usuario y procesamiento de archivos:
```sh
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/hduser
hdfs dfs -mkdir input
```

Permisos 
```sh
sudo chown -R hduser .
```

Carga de los documentos a procesar en hadoop
```sh
cd app/
hdfs dfs -put carpeta1/*.txt input
hdfs dfs -put carpeta2/*.txt input
```

Validación
```sh
hdfs dfs -ls input
```

Ejecución map-reducer
```sh
mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output hduser/outhadoop/ -mapper ./mapper.py -reducer ./reducer.py
```

Exportacion del archivo procesado
```sh
hdfs dfs -get /user/hduser/hduser/outhadoop/ /home/hduser/app
```

Salir del contenedor
```sh
exit
```

Buscar palabra en el archivo procesado:
```sh
python3 search.py "palabra_a_buscar"
```

## Video de instalación, uso y explicación

[![Watch the video](https://img.youtube.com/vi/U7_dAycum9I/hqdefault.jpg)](https://youtu.be/U7_dAycum9I)
