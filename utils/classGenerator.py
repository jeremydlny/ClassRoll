import random
from .jsonLoader import load_json_data

# Chargement des données
armes_data = load_json_data('armes.json')
atouts_data = load_json_data('atouts.json')
equipements_data = load_json_data('equipements.json')
defis_data = load_json_data('defis.json')

def safe_list(d, key):
    v = d.get(key)
    if isinstance(v, list):
        return v
    return []

# Maps des catégories (constantes)
CATEGORY_KEY_MAP = {
    # Armes principales
    "Fusils d'assaut": "fusils_d_assaut",
    "Mitraillettes": "mitraillettes",
    "Fusils à pompe": "fusils_a_pompe",
    "Mitrailleuses": "mitrailleuses",
    "Fusils tactiques": "fusils_tactiques",
    "Fusils de précision": "fusils_de_precision",
    # Armes secondaires
    "Pistolets": "pistolets",
    "Lanceurs": "lanceurs",
    "Spécial": "special"
}

# Cache pour les armes
_armes_cache = {
    'principales': {},
    'secondaires': {}
}

def _init_cache():
    """Initialise le cache des armes"""
    global _armes_cache
    
    # Cache des armes principales
    if "principales" in armes_data:
        for display_name, key in CATEGORY_KEY_MAP.items():
            if key in armes_data["principales"]:
                _armes_cache['principales'][display_name] = armes_data["principales"][key]
    
    # Cache des armes secondaires
    if "secondaires" in armes_data:
        for display_name, key in CATEGORY_KEY_MAP.items():
            if key in armes_data["secondaires"]:
                _armes_cache['secondaires'][display_name] = armes_data["secondaires"][key]

_init_cache()

def find_category_list(category):
    """Retourne la liste des armes d'une catégorie donnée depuis le cache"""
    # Cherche d'abord dans les armes principales
    if category in _armes_cache['principales']:
        return _armes_cache['principales'][category]
    # Sinon cherche dans les armes secondaires
    if category in _armes_cache['secondaires']:
        return _armes_cache['secondaires'][category]
    return []

def generer_arme_aleatoire():
    """Fonction simplifiée pour générer une arme aléatoire"""
    toutes_armes = []
    if "principales" in armes_data:
        for categorie, armes in armes_data["principales"].items():
            if isinstance(armes, list):
                toutes_armes.extend(armes)
    if "secondaires" in armes_data:
        for categorie, armes in armes_data["secondaires"].items():
            if isinstance(armes, list):
                toutes_armes.extend(armes)
    return random.choice(toutes_armes) if toutes_armes else "Aucune arme disponible"

def generer_arme_principale():
    """Génère uniquement une arme principale"""
    armes_principales = []
    if "principales" in armes_data:
        for categorie, armes in armes_data["principales"].items():
            if isinstance(armes, list):
                armes_principales.extend(armes)
    return random.choice(armes_principales) if armes_principales else "Aucune arme principale"

def generer_arme_secondaire():
    """Génère uniquement une arme secondaire"""
    armes_secondaires = []
    if "secondaires" in armes_data:
        for categorie, armes in armes_data["secondaires"].items():
            if isinstance(armes, list):
                armes_secondaires.extend(armes)
    return random.choice(armes_secondaires) if armes_secondaires else "Aucune arme secondaire"

# Cache pour les listes d'armes et d'équipements
_CACHE = {
    'armes_principales': [],
    'armes_secondaires': [],
    'atouts_1': [],
    'atouts_2': [],
    'atouts_3': [],
    'tactiques': [],
    'mortels': []
}

def _refresh_cache():
    """Rafraîchit le cache des armes et équipements"""
    global _CACHE
    
    # Armes principales
    _CACHE['armes_principales'] = []
    for categorie in armes_data.get("principales", {}).values():
        if isinstance(categorie, list):
            _CACHE['armes_principales'].extend(categorie)
    
    # Armes secondaires
    _CACHE['armes_secondaires'] = []
    for categorie in armes_data.get("secondaires", {}).values():
        if isinstance(categorie, list):
            _CACHE['armes_secondaires'].extend(categorie)
    
    # Atouts et équipements
    _CACHE['atouts_1'] = safe_list(atouts_data, 'atout_1')
    _CACHE['atouts_2'] = safe_list(atouts_data, 'atout_2')
    _CACHE['atouts_3'] = safe_list(atouts_data, 'atout_3')
    _CACHE['tactiques'] = safe_list(equipements_data, 'tactiques')
    _CACHE['mortels'] = safe_list(equipements_data, 'mortels')

_refresh_cache()

def generer_classe():
    """Générer une classe BO6 avec 1 atout par slot (si disponible)."""
    # Sélection arme principale (plus rapide sans condition)
    arme_principale = random.choice(_CACHE['armes_principales']) if _CACHE['armes_principales'] else "Aucune arme principale disponible"

    # Sélection arme secondaire optimisée (évite les doublons sans créer de set)
    if _CACHE['armes_secondaires']:
        # Essayer d'abord de prendre dans les armes secondaires
        arme_secondaire = random.choice(_CACHE['armes_secondaires'])
        # Si c'est la même que la principale, réessayer une fois
        if arme_secondaire == arme_principale and len(_CACHE['armes_secondaires']) > 1:
            autres = [a for a in _CACHE['armes_secondaires'] if a != arme_principale]
            if autres:
                arme_secondaire = random.choice(autres)
    else:
        arme_secondaire = "Aucune arme secondaire disponible"

    return {
        "arme_principale": arme_principale,
        "arme_secondaire": arme_secondaire,
        "atout_1": random.choice(_CACHE['atouts_1']) if _CACHE['atouts_1'] else "Aucun atout slot 1",
        "atout_2": random.choice(_CACHE['atouts_2']) if _CACHE['atouts_2'] else "Aucun atout slot 2",
        "atout_3": random.choice(_CACHE['atouts_3']) if _CACHE['atouts_3'] else "Aucun atout slot 3",
        "equipement_tactique": random.choice(_CACHE['tactiques']) if _CACHE['tactiques'] else "Aucun équipement tactique",
        "equipement_mortel": random.choice(_CACHE['mortels']) if _CACHE['mortels'] else "Aucun équipement mortel"
    }
