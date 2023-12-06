import bot
import sys

if __name__ == '__main__':
    # comprobamos que los datos se han recibido
    if len(sys.argv) != 3:
        print('No se han recibido los parámetros necesarios: TOKEN, CHANNEL_ID')
        sys.exit(1)
    
    TOKEN = sys.argv[1]
    CHANNEL_ID = sys.argv[2]
    
    print(f'{TOKEN} ; {CHANNEL_ID}')  
    
    # ejecutamos el bot
    bot.run_discord_bot(TOKEN, CHANNEL_ID)