import os
import sys

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import spécifique du fichier bot.py (pas du dossier bot/)
import importlib.util
spec = importlib.util.spec_from_file_location("bot_module", "bot.py")
bot_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bot_module)

if __name__ == "__main__":
    bot_module.start_bot()
