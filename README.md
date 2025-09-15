# ClassRoll - Bot Discord pour la générati## Permissions Discord

Le bot doit avoir les permissions suivantes sur ton serveur :

- Gérer les messages
- Utiliser les slash commands
- Lire et envoyer des messages
- **Écriture dans le salon `classe`** (pour la sauvegarde)
- **Administrateur** (pour utiliser `/reload`)asses et défis

ClassRoll est un bot Discord écrit en Python qui permet de générer des classes aléatoires, des armes, des équipements et des défis pour des jeux de tir (type Call of Duty). Il propose une interface interactive avec des boutons, des vues personnalisées et des commandes slash.

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
  - `/roll` → Donne une classe générée aléatoirement avec la possibilité de la sauvarger
  - `/arme` → Donne une arme générée aléatoirement avec la possibilité de la sauvarger
  - `/principale` → Donne une arme générée aléatoirement avec la possibilité de la sauvarger
  - `/secondaire` → Donne une arme générée aléatoirement avec la possibilité de la sauvarger
  - `/défis` → Donne un défi générée aléatoirement avec la possibilité de la sauvarger

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

## Permissions Discord

Le bot doit avoir les permissions suivantes sur ton serveur :

- Gérer les messages
- Utiliser les slash commands
- Lire et envoyer des messages
- **Administrateur** (pour synchroniser les commandes avec `/sync`)

## Personnalisation

- Modifie les fichiers JSON dans le dossier `Data/` pour ajouter ou retirer des armes, atouts, équipements ou défis.

## Contribution

Les contributions sont les bienvenues ! N’hésite pas à ouvrir une issue ou une pull request.

## Licence

Ce projet est open-source sous licence MIT.

---

**Contact** : Pour toute question ou suggestion, ouvre une issue sur le dépôt ou contacte le créateur sur Discord.
