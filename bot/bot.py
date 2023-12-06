import asyncio
import discord
import respuestas   
import chistes   

# Esta función obtiene el token desde un fichero de texto externo 
def get_token() -> str:
    f = open('info-bot.txt' , 'r')
    content = f.readline()
    
    return content
        
def run_discord_bot():
    # Variables para la ejecución
    TOKEN = get_token() # Token del bot
    # Creación del cliente
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    print(f'Poniendo en marcha... {TOKEN}')
    
    # Lógica del bot debajo
    
    # Este trozo de código espera un tiempo determinado para contar un chiste
    async def send_joke():
        time = 2 # tiempo en segundos
        channel_id = 1181912230871191575 # esto hay que ir cambiándolo en función del canal
        channel = client.get_channel(channel_id)
        
        while True: # Este bucle espera el tiempo estipulado
            chiste = await chistes.get_joke()
        
            if channel:
                await channel.send(chiste)
                
            await asyncio.sleep(time)
    
    @client.event
    async def on_ready():
        print(f'{client.user} está funcionando')
        
        # loop para el envío de chistes
        client.loop.create_task(send_joke())
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        # Debug
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f'{username} escribió: "{user_message}" en el canal: {channel}')
        
        await send_message(message, user_message)
        
    # Ejecución del bot
    client.run(TOKEN)

# Esta función manda un mensaje en función del mensaje que reciba
async def send_message(message, user_message):
    try:
        response = respuestas.handle_response(user_message)
        if response is not None: 
            await message.channel.send(response)
    except Exception as e:
        print(e)