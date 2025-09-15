# ClassRoll - Bot Discord pour la générati## Permissions Discord

Le bot doit avoir les permissions suivantes sur ton serveur :

- Gérer les messages
- Utiliser les slash commands
- Lire et envoyer des messages
- **Écriture dans le salon `classe`** (pour la sauvegarde)
- **Administrateur** (pour utiliser `/reload`)asses et défis

ClassRoll est un bot Discord écrit en JavaScript (discord.js) qui permet de générer des classes aléatoires, des armes, des équipements et des défis pour des jeux de tir (type Call of Duty). Il propose une interface interactive avec des boutons, des vues personnalisées et des commandes slash.

> **🔄 Version JavaScript**: Cette branche `developjs` contient la version JavaScript du bot, convertie depuis la version Python originale.

## Fonctionnalités principales

- `/roll` : Génère une classe complète (arme principale, secondaire, atouts, équipements)
- `/principale` : Choisis une arme principale par catégorie
- `/secondaire` : Choisis une arme secondaire par catégorie
- `/défis` : Propose des défis aléatoires selon la difficulté
- `/aide` : Affiche l'aide du bot
- `/delete` : Supprime tous les messages du bot dans le salon
- `/reload` : Recharge les commandes du bot (réservé aux administrateurs)

## 💾 Fonctionnalité de Sauvegarde

**Le bot dispose d'une fonctionnalité de sauvegarde automatique dans un salon dédié :**

### Configuration requise

1. **Créez un salon textuel** nommé exactement `🔫・classe` sur votre serveur Discord
2. **Assurez-vous** que le bot a les permissions d'écriture dans ce salon

### Comment ça fonctionne

- **Bouton SAUVEGARDER** disponible dans toutes les interfaces :
  - `/roll` → Sauvegarde la classe complète
  - `/principale` → Sauvegarde l'arme principale générée
  - `/secondaire` → Sauvegarde l'arme secondaire générée
  - `/défis` → Sauvegarde le défi choisi
  - Interface "ARME SEULE" → Sauvegarde l'arme aléatoire

### Utilisation

1. Générez votre classe/arme/défi avec les commandes habituelles
2. Cliquez sur le bouton **SAUVEGARDER**
3. Le contenu est automatiquement envoyé dans le salon `#🔫・classe`
4. **Aucune notification** - la sauvegarde est silencieuse

### Format de sauvegarde

- **Embed vert** avec titre explicite (ex: "💾 Classe Sauvegardée")
- **Mention** de qui a sauvegardé
- **Contenu complet** formaté proprement
- **Footer** indiquant le salon d'origine

## Installation et configuration

### Prérequis
- Node.js 18.0.0 ou plus récent
- npm (inclus avec Node.js)
- Un bot Discord configuré

### Installation

1. Clonez le dépôt et basculez sur la branche JavaScript :
```bash
git clone https://github.com/jeremydlny/ClassRoll.git
cd ClassRoll
git checkout developjs
```

2. Installez les dépendances :
```bash
npm install
```

3. Configurez les variables d'environnement :
```bash
cp .env.example .env
```
Éditez le fichier `.env` et ajoutez votre token Discord :
```
DISCORD_BOT_TOKEN=votre_token_ici
```

4. Démarrez le bot :
```bash
npm start
```

Pour le développement avec rechargement automatique :
```bash
npm run dev
```

## Permissions Discord

Le bot doit avoir les permissions suivantes sur ton serveur :

- Gérer les messages
- Utiliser les slash commands
- Lire et envoyer des messages
- **Administrateur** (pour synchroniser les commandes avec `/sync`)

## Structure du projet

```
ClassRoll/
├── commands/           # Configuration des commandes slash
├── views/             # Interfaces Discord (boutons, menus)
├── utils/             # Utilitaires (générateur, logger, stats)
├── Data/              # Fichiers JSON avec les données du jeu
├── index.js           # Point d'entrée principal
├── package.json       # Dépendances et scripts npm
└── .env.example       # Template pour les variables d'environnement
```

## Personnalisation

- Modifie les fichiers JSON dans le dossier `Data/` pour ajouter ou retirer des armes, atouts, équipements ou défis.

## Développement

### Scripts disponibles
- `npm start` : Démarre le bot
- `npm run dev` : Démarre avec rechargement automatique

### Technologies utilisées
- **discord.js v14** : Librairie Discord pour JavaScript
- **Node.js ES Modules** : Syntaxe import/export moderne
- **dotenv** : Gestion des variables d'environnement

## Contribution

Les contributions sont les bienvenues ! N’hésite pas à ouvrir une issue ou une pull request.

## Licence

Ce projet est open-source sous licence MIT.

---

**Contact** : Pour toute question ou suggestion, ouvre une issue sur le dépôt ou contacte le créateur sur Discord.
