import os
import json
from datetime import datetime
import logging
from functools import lru_cache

logger = logging.getLogger(__name__)

# Cache pour les stats afin d'éviter de lire le fichier à chaque fois
_stats_cache = None
_stats_file_path = os.path.join('Data', 'stats.json')  # Correction du chemin

def _load_stats():
    """Charge les statistiques depuis le fichier"""
    global _stats_cache
    try:
        with open(_stats_file_path, 'r', encoding='utf-8') as f:
            _stats_cache = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        _stats_cache = {}
    return _stats_cache

def _save_stats():
    """Sauvegarde les statistiques dans le fichier"""
    if _stats_cache is None:
        return
    try:
        # Créer le dossier si nécessaire
        os.makedirs(os.path.dirname(_stats_file_path), exist_ok=True)
        with open(_stats_file_path, 'w', encoding='utf-8') as f:
            json.dump(_stats_cache, f, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.warning(f"Impossible de sauvegarder les stats: {e}")

def update_stats(command):
    """Mettre à jour les statistiques d'utilisation (optimisé)"""
    global _stats_cache
    
    # Charger le cache si nécessaire
    if _stats_cache is None:
        _load_stats()
    
    # Mettre à jour en mémoire
    _stats_cache[command] = _stats_cache.get(command, 0) + 1
    _stats_cache['last_used'] = datetime.now().isoformat()
    
    # Sauvegarder (de manière asynchrone serait encore mieux)
    _save_stats()
