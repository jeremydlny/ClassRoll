# ClassRoll - Bot Discord pour la génération de classes et défis

ClassRoll est un bot Discord écrit en Python qui permet de générer des classes aléatoires, des armes, des équipements et des défis pour des jeux de tir (type Call of Duty). Il propose une interface interactive avec des boutons, des vues personnalisées et des commandes slash.

## Fonctionnalités principales

- `/roll` : Génère une classe complète (arme principale, secondaire, atouts, équipements)
- `/principale` : Choisis une arme principale par catégorie
- `/secondaire` : Choisis une arme secondaire par catégorie
- `/défis` : Propose des défis aléatoires selon la difficulté
- `/aide` : Affiche l'aide du bot
- `/sync` : Synchronise les commandes du bot (réservé aux administrateurs)

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
