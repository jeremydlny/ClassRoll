import { EmbedBuilder } from 'discord.js';

/**
 * Create embed for help/aide command
 * @returns {EmbedBuilder} Discord embed
 */
export function createAideEmbed() {
    return new EmbedBuilder()
        .setTitle('📖 Aide - ClassRoll Bot')
        .setDescription('**Bot Discord pour la génération de classes et défis Call of Duty Black Ops 6**')
        .setColor(0x0099ff)
        .setTimestamp()
        .addFields(
            {
                name: '🎲 Commandes principales',
                value: '```/roll - Génère une classe complète aléatoire\n/principale - Choisir une arme principale par catégorie\n/secondaire - Choisir une arme secondaire par catégorie\n/défis - Proposer des défis aléatoires selon la difficulté\n/aide - Afficher cette aide```',
                inline: false
            },
            {
                name: '🔧 Commandes administrateur',
                value: '```/sync - Synchroniser les commandes du bot\n/delete - Supprimer tous les messages du bot```',
                inline: false
            },
            {
                name: '🎯 Fonctionnalités',
                value: '• **Classes complètes** : Arme principale, secondaire, 3 atouts, équipements\n• **Armes par catégorie** : Choisissez le type d\'arme que vous voulez\n• **Défis variés** : Plusieurs niveaux de difficulté disponibles\n• **Interface interactive** : Boutons pour re-roll, défis, etc.',
                inline: false
            },
            {
                name: '🛠️ Permissions requises',
                value: '• Gérer les messages\n• Utiliser les slash commands\n• Lire et envoyer des messages\n• **Administrateur** (pour synchroniser avec `/sync`)',
                inline: false
            },
            {
                name: '📁 Personnalisation',
                value: 'Modifiez les fichiers JSON dans le dossier `Data/` pour ajouter ou retirer des armes, atouts, équipements ou défis.',
                inline: false
            }
        )
        .setFooter({ text: '🎮 Bot créé pour Call of Duty: Black Ops 6 | Open Source sous licence MIT' });
}

/**
 * Create the help view (no interactive components needed for now)
 * @returns {Object} Empty components object
 */
export function createAideView() {
    return { components: [] };
}