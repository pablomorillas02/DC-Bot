import chistes

async def handle_response(message: str) -> str:
    text = message.lower()
    
    if text == 'hola':
        return 'Hola'
    
    if 'pozas' in text:
        return 'Que mal me cae Pozas'
    
    if 'maria' in text:
        return 'Que mal me cae María Pozas'
    
    if text == 'amo a maria':
        return 'Yo también'
    
    if 'hugo' in text:
        return 'Hugo maricón'
    
    if 'cj' in text:
        return 'CJ fuera del server'
    
    if 'pablo' in text:
        return 'Pablo es guapo, listo y atlético, todo un semental'
    
    if 'juanma' in text:
        return 'Juanma baiter de época'
    
    if text == '_chiste':
        return await chistes.get_joke()
    
    if text == '_help':
        return '`Soy un bot creador por Pablo, lo único que hago es poner chistes cada cierto tiempo y contestar a algunos mensajes.`'