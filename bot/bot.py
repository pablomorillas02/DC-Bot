import discord
import respuestas      

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
    
    print(f'Poniendo en marcha... ({TOKEN})')
    
    # Lógica del bot debajo
    
    @client.event
    async def on_ready():
        print(f'{client.user} está funcionando')
    
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