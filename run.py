import os
import sys

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import direct maintenant que le dossier bot/ conflictuel est supprimé
from bot import start_bot

if __name__ == "__main__":
    start_bot()
