from discord.ext import commands
import discord
import logging
from commands import setup

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

@bot.event
async def on_ready():
    logging.info(f"✅ Bot connecté: {bot.user} (ID: {bot.user.id if bot.user else 'N/A'})")
    try:
        await setup(bot)  # Setup des commandes
        synced = await bot.tree.sync()  # Synchronisation des commandes
        logging.info(f"✅ {len(synced)} commandes synchronisées")
    except Exception as e:
        logging.exception("❌ Erreur sync commandes:")

bot_instance = bot
