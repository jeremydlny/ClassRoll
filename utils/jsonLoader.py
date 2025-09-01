import os
import json
import logging
from functools import lru_cache

logger = logging.getLogger(__name__)

@lru_cache(maxsize=32)
def load_json_data(filename):
    """Charge un fichier JSON depuis le dossier data/ avec mise en cache ; retourne {} si erreur."""
    path = os.path.join('data', filename)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning(f"⚠️ Fichier non trouvé: {path}")
        return {}
    except json.JSONDecodeError as e:
        logger.warning(f"⚠️ JSON invalide dans {path}: {e}")
        return {}
    except Exception as e:
        logger.exception(f"Erreur lecture {path}: {e}")
        return {}
