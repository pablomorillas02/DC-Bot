# Este módulo temporiza el tiempo para mandar chistes, además de elegirlos de un fichero de texto de manera pseudoaleatoria
import random

async def get_joke() -> str:
    try:
        with open('jokes.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if lines:
            random_line = random.choice(lines)
            return random_line.strip()
        else:
            return None
        
    except Exception as e:
        print(f'Ocurrió un error al obtener el chiste: {str(e)}')
        return None