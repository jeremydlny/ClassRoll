import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils.logger import logger

# Configuration des intents
intents = discord.Intents.default()
intents.message_content = True  # Pour lire le contenu des messages
intents.members = True         # Pour accéder aux membres
intents.guilds = True         # Pour accéder aux serveurs

# Configuration des permissions
permissions = discord.Permissions()
permissions.manage_messages = True  # Pour gérer les messages

# Création du bot avec les intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Charger les variables d'environnement depuis _env/.env
env_path = os.path.join(os.path.dirname(__file__), '_env', '.env')
load_dotenv(env_path)

@bot.event
async def on_ready():
    logger.info(f"✅ Bot connecté: {bot.user} (ID: {bot.user.id if bot.user else 'N/A'})")
    try:
        from commands import setup
        await setup(bot)
        synced = await bot.tree.sync()
        logger.info(f"✅ {len(synced)} commandes synchronisées")
    except Exception as e:
        logger.exception("❌ Erreur sync commandes:")

def start_bot():
    """Start the Discord bot"""
    discord_token = os.getenv("DISCORD_BOT_TOKEN")
    if not discord_token:
        logger.error("DISCORD_BOT_TOKEN non trouvé dans _env/.env")
        return
    try:
        bot.run(discord_token)
    except Exception as e:
        logger.exception("❌ Erreur lors du démarrage du bot:")
