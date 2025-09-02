import { ActionRowBuilder, StringSelectMenuBuilder, EmbedBuilder } from 'discord.js';
import { defisData } from '../utils/classGenerator.js';
import { getRandomChoice } from '../utils/random.js';

/**
 * Create embed for challenges selection
 * @returns {EmbedBuilder} Discord embed
 */
export function createDefiEmbed() {
    const embed = new EmbedBuilder()
        .setTitle('🏆 Choisissez votre défi !')
        .setDescription('Sélectionnez le niveau de difficulté :')
        .setColor(0xff4444)
        .setTimestamp();

    // Add fields for each difficulty level
    for (const [niveau, defisList] of Object.entries(defisData)) {
        if (Array.isArray(defisList)) {
            embed.addFields({
                name: niveau.charAt(0).toUpperCase() + niveau.slice(1),
                value: `\`\`\`${defisList.length} défis disponibles\`\`\``,
                inline: true
            });
        }
    }

    return embed;
}

/**
 * Create the challenges selection view
 * @param {Object} classe - Current class data (for potential return navigation)
 * @returns {Object} Components for the message
 */
export function createDefiView(classe = null) {
    const options = [];

    // Add difficulty options based on available challenges
    for (const [niveau, defisList] of Object.entries(defisData)) {
        if (Array.isArray(defisList) && defisList.length > 0) {
            let emoji = '🎯';
            let description = 'Niveau de difficulté standard';
            
            switch (niveau.toLowerCase()) {
                case 'facile':
                    emoji = '🟢';
                    description = 'Défis accessibles pour débuter';
                    break;
                case 'moyen':
                    emoji = '🟡';
                    description = 'Défis de difficulté modérée';
                    break;
                case 'difficile':
                    emoji = '🔴';
                    description = 'Défis challenging pour experts';
                    break;
                case 'extreme':
                    emoji = '🟣';
                    description = 'Défis extrêmes pour les pros';
                    break;
            }

            options.push({
                label: niveau.charAt(0).toUpperCase() + niveau.slice(1),
                description: description,
                value: niveau,
                emoji: emoji
            });
        }
    }

    const selectMenu = new StringSelectMenuBuilder()
        .setCustomId('select_defi')
        .setPlaceholder('Choisissez un niveau de difficulté')
        .addOptions(options);

    const row = new ActionRowBuilder()
        .addComponents(selectMenu);

    return { components: [row] };
}

/**
 * Handle challenge selection interaction
 * @param {Interaction} interaction - Discord interaction
 */
export async function handleDefiSelection(interaction) {
    const selectedDifficulty = interaction.values[0];
    const challenges = defisData[selectedDifficulty];
    
    if (!Array.isArray(challenges) || challenges.length === 0) {
        await interaction.reply({
            content: `❌ Aucun défi trouvé pour la difficulté "${selectedDifficulty}"`,
            ephemeral: true
        });
        return;
    }

    const selectedChallenge = getRandomChoice(challenges);
    
    // Determine color based on difficulty
    let color = 0x00ff00;
    let difficultyIcon = '🎯';
    
    switch (selectedDifficulty.toLowerCase()) {
        case 'facile':
            color = 0x00ff00;
            difficultyIcon = '🟢';
            break;
        case 'moyen':
            color = 0xffff00;
            difficultyIcon = '🟡';
            break;
        case 'difficile':
            color = 0xff8800;
            difficultyIcon = '🔴';
            break;
        case 'extreme':
            color = 0xff0088;
            difficultyIcon = '🟣';
            break;
    }
    
    const embed = new EmbedBuilder()
        .setTitle(`🏆 Défi ${selectedDifficulty.charAt(0).toUpperCase() + selectedDifficulty.slice(1)}`)
        .setDescription(`Votre défi aléatoire :`)
        .setColor(color)
        .setTimestamp()
        .addFields({
            name: `${difficultyIcon} Votre mission`,
            value: `\`\`\`${selectedChallenge}\`\`\``,
            inline: false
        })
        .setFooter({ text: '🎯 Relevez le défi !' });

    await interaction.update({ embeds: [embed], components: [] });
}