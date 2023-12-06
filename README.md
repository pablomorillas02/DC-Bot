# Bot
### Funcionamiento básico
Este bot de Discord implementado en python simplemente hace dos cosas. Contestar a cierto tipo de mensajes y contar un chiste malo cada cierto tiempo de manera pseudoaleatoria.

#### ¿Cómo cuenta los chistes?
Pues bien, cada cierto tiempo, se lanzará un dado de un número de caras determinado por el usuario, si la probabilidad se cumple, se contará un chiste elegido de manera aleatoria de una lista, en caso contrario, se volverá a esperar el tiempo previamente determinado.

Posteriormente se explicará como configurar dichos parámetros.

## Preparación y ejecución
Para poder ejecutar tu propia versión del bot tendrás que generar un token y un link de invitación al servidor, dentro de los archivos ya se encuentra un token (inservible, tienes que generar uno propio y mantenerlo privado) y un link de invitación.

Una vez hayas añadido el bot a tu servidor, tendrás que copiar el ID del canal y el token del bot y pegarlos en el archivo batch de la siguiente forma:
> python /code/main.py TOKEN CHANNEL_ID

Para configurar la frecuencia para el conteo de chistes, hay una carpeta (_data_) con todos los archivos de configuración necesarios para su ejecución.

* **Chistes**: El archivo _jokes.txt_ contiene un listado de todos los posibles chistes que el bot puede contar
* **Frecuencia**: El archivo _config.txt_ contiene todos los parámetros necesarios para la frecuencia con la que se cuenta un chiste (tiempo y probabilidad)
* El archivo _bot-data.txt_ simplemente contiene información importante relativa al bot.
