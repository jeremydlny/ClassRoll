import os
import logging
from dotenv import load_dotenv
from bot import bot

logger = logging.getLogger(__name__)

# Charger les variables d'environnement depuis _env/.env
env_path = os.path.join(os.path.dirname(__file__), '_env', '.env')
load_dotenv(env_path)

def start_bot():
    """Start the Discord bot"""
    discord_token = os.getenv("DISCORD_BOT_TOKEN")
    if not discord_token:
        logging.error("DISCORD_BOT_TOKEN non trouvé dans _env/.env")
        return
    try:
        bot.run(discord_token)
    except Exception as e:
        logging.error(f"Erreur lors du démarrage du bot: {e}")

if __name__ == "__main__":
    start_bot()
