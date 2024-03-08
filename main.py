"""
Basic example for a bot that can send polls to a channel.
"""

import os
import asyncio
from telegram import Bot
from telegram.error import NetworkError
import logging
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv('TOKEN')

# Configuration du logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


async def send_poll_to_channel(channel_id: str, question: str, options: list):
    """Fonction pour envoyer un sondage.
    
    Args:
        channel_id (str): ID du channel où envoyer le sondage.
        question (str): Question du sondage.
        options (list): Liste des options du sondage.
        
    Returns:
        None
    """
    bot = Bot(TOKEN)
    try:
        # Création et envoi du sondage
        await bot.send_poll(chat_id=channel_id, question=question, options=options, is_anonymous=False)
        logger.info("Sondage envoyé avec succès.")
    except (NetworkError) as e:
        logger.error(f"Erreur lors de l'envoi du sondage : {e}")

if __name__ == '__main__':
    question = "Comment vous sentez-vous aujourd'hui ?"
    options = ["Heureux", "Triste", "Fatigué", "Excité"]
    CHANNEL_ID = os.getenv('CHANNEL_ID')
    asyncio.run(send_poll_to_channel(CHANNEL_ID, question, options))
