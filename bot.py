# Point d'entrée pour le bot Discord
from bot import bot, bot_instance
from utils.logger import logger

# Setup des commandes
from commands import setup

@bot.event
async def on_ready():
    logger.info(f"✅ Bot connecté: {bot.user} (ID: {bot.user.id if bot.user else 'N/A'})")
    try:
        await setup(bot)
        synced = await bot.tree.sync()
        logger.info(f"✅ {len(synced)} commandes synchronisées")
    except Exception as e:
        logger.exception("❌ Erreur sync commandes:")

def start_bot():
    """Start the Discord bot"""
    from run import start_bot as run_bot
    run_bot()
