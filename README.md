# ClassRoll - Bot Discord pour la génération de classes et défis

ClassRoll est un bot Discord écrit en Python qui permet de générer des classes aléatoires, des armes, des équipements et des défis pour des jeux de tir (type Call of Duty). Il propose une interface interactive avec des boutons, des vues personnalisées et des commandes slash.

## Fonctionnalités principales

- `/roll` : Génère une classe complète (arme principale, secondaire, atouts, équipements)
- `/principale` : Choisis une arme principale par catégorie
- `/secondaire` : Choisis une arme secondaire par catégorie
- `/défis` : Propose des défis aléatoires selon la difficulté
- `/aide` : Affiche l'aide du bot

## Navigation interactive

- Boutons pour relancer une classe, afficher une arme seule, choisir un défi, ou revenir en arrière
- Vues personnalisées pour chaque catégorie d'arme et chaque niveau de défi
- Embeds colorés et organisés pour une meilleure lisibilité

## Installation

1. **Cloner le projet**

   ```bash
   git clone https://github.com/ton-utilisateur/ClassRoll.git
   cd ClassRoll
   ```

2. **Installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer le token Discord**

   - Crée un dossier `_env` à la racine du projet
   - Ajoute un fichier `.env` contenant :
     ```
     DISCORD_BOT_TOKEN=ton_token_discord_ici
     ```

4. **Lancer le bot**
   ```bash
   python run.py
   ```

## Structure du projet

```
ClassRoll/
├── bot.py
├── run.py
├── _env/
│   └── .env
├── Data/
│   ├── armes.json
│   ├── atouts.json
│   ├── defis.json
│   ├── equipements.json
│   └── stats.json
├── utils/
│   ├── classGenerator.py
│   ├── jsonLoader.py
│   ├── logger.py
│   ├── random.py
│   ├── stats.py
│   └── __init__.py
├── views/
│   ├── principaleView.py
│   ├── secondaireView.py
│   ├── rollView.py
│   ├── armeView.py
│   ├── defiView.py
│   ├── aideView.py
│   └── __init__.py
├── commands/
│   └── __init__.py
```

## Personnalisation

- Modifie les fichiers JSON dans `Data/` pour ajouter ou retirer des armes, atouts, équipements ou défis.
- Les vues et boutons sont personnalisables dans le dossier `views/`.

## Permissions Discord

- Le bot doit avoir les permissions suivantes sur ton serveur :
  - Gérer les messages
  - Utiliser les slash commands
  - Lire les messages et envoyer des messages
  - **Administrateur** (requis pour synchroniser les commandes avec `/sync`)

## Contribution

Les contributions sont les bienvenues ! N’hésite pas à ouvrir une issue ou une pull request.

## Licence

Ce projet est open-source sous licence MIT.
