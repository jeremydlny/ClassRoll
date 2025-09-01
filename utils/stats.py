import os
import json
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def update_stats(command):
    """Mettre à jour les statistiques d'utilisation"""
    stats_file = os.path.join('data', 'stats.json')
    try:
        with open(stats_file, 'r', encoding='utf-8') as f:
            stats = json.load(f)
    except FileNotFoundError:
        stats = {}
    except json.JSONDecodeError:
        stats = {}

    stats[command] = stats.get(command, 0) + 1
    stats['last_used'] = datetime.now().isoformat()

    try:
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.warning(f"Impossible de sauvegarder les stats: {e}")
