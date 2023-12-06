def handle_response(message: str) -> str:
    text = message.lower()
    
    if text == 'hola':
        return 'Hola'
    
    if text == 'pozas':
        return 'Amo a maría'
    
    if text == '_help':
        return '`Soy un bot creador por Pablo, lo único que hago es poner mensajes cada cierto tiempo y contestar a algunos mensajes.`'