import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'Hello Bot!':
        return 'Hello!'

    if p_message == 'Help Me':
        return 'A bot can only do so much.'
   
