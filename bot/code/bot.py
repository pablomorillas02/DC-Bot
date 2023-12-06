import asyncio
import discord
import respuestas
import chistes
import random   

# Esta función extrae todas las configuraciones temporales y probabilísticas de un fichero de texto externo
def get_config():
    with open('data/config.txt', 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            if 'jokes_trigger' in line:
                jokes_trigger = int(line.split("=")[1].strip())
            if 'time' in line:
                time = int(line.split("=")[1].strip())
    
    return jokes_trigger, time
            
        
def run_discord_bot(TOKEN, CHANNEL_ID):
    # Variables configurables
    jokes_trigger, time = get_config()
    
    # Creación del cliente
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    print(f'Poniendo en marcha... {TOKEN}')
    
    # Lógica del bot debajo # 
    
    # Este trozo de código espera un tiempo determinado para contar un chiste
    async def send_joke():
        channel_id = int(CHANNEL_ID) # esto hay que ir cambiándolo en función del canal
        channel = client.get_channel(channel_id)
        
        while True: # Este bucle espera el tiempo estipulado
            joke = await chistes.get_joke()
        
            roll = random.randint(1, jokes_trigger) # probabilidad de que se mande el chiste
        
            if roll == 1:
                print(f'Se va mandar un chiste (probabilidad de 1 sobre {jokes_trigger})')
                if channel:
                    if joke is not None:
                        await channel.send(joke)
                
            await asyncio.sleep(time)
    
    # Evento de arranque
    @client.event
    async def on_ready():
        print(f'{client.user} está funcionando')
        
        # loop para el envío de chistes
        client.loop.create_task(send_joke())
    
    # Evento para mandar un mensaje si se manda uno en concreto
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
        response = await respuestas.handle_response(user_message)
        if response is not None: 
            await message.channel.send(response)
    except Exception as e:
        print(e)