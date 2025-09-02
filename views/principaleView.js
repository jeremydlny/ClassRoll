import { ActionRowBuilder, StringSelectMenuBuilder, EmbedBuilder } from 'discord.js';
import { findCategoryList } from '../utils/classGenerator.js';
import { getRandomChoice } from '../utils/random.js';

/**
 * Create embed for primary weapons selection
 * @returns {EmbedBuilder} Discord embed
 */
export function createPrincipaleEmbed() {
    return new EmbedBuilder()
        .setTitle('🔫 Armes principales')
        .setDescription('```Choisissez une catégorie pour obtenir une arme aléatoire dedans.```')
        .setColor(0x00ccff)
        .setTimestamp();
}

/**
 * Create the primary weapons selection view
 * @returns {Object} Components for the message
 */
export function createPrincipaleView() {
    const selectMenu = new StringSelectMenuBuilder()
        .setCustomId('select_principale')
        .setPlaceholder('Choisissez une catégorie d\'arme principale')
        .addOptions([
            {
                label: 'Fusils d\'assaut',
                description: 'Armes polyvalentes pour tous types de combat',
                value: 'Fusils d\'assaut',
                emoji: '🔫'
            },
            {
                label: 'Mitraillettes',
                description: 'Armes rapides pour le combat rapproché',
                value: 'Mitraillettes',
                emoji: '🏃'
            },
            {
                label: 'Fusils à pompe',
                description: 'Armes dévastatrices à courte portée',
                value: 'Fusils à pompe',
                emoji: '💥'
            },
            {
                label: 'Mitrailleuses',
                description: 'Armes lourdes avec beaucoup de munitions',
                value: 'Mitrailleuses',
                emoji: '🔥'
            },
            {
                label: 'Fusils tactiques',
                description: 'Armes précises pour le combat à moyenne portée',
                value: 'Fusils tactiques',
                emoji: '🎯'
            },
            {
                label: 'Fusils de précision',
                description: 'Armes à longue portée pour les tirs précis',
                value: 'Fusils de précision',
                emoji: '🎭'
            }
        ]);

    const row = new ActionRowBuilder()
        .addComponents(selectMenu);

    return { components: [row] };
}

/**
 * Handle primary weapon selection interaction
 * @param {Interaction} interaction - Discord interaction
 */
export async function handlePrincipaleSelection(interaction) {
    const selectedCategory = interaction.values[0];
    const weapons = findCategoryList(selectedCategory);
    
    if (weapons.length === 0) {
        await interaction.reply({
            content: `❌ Aucune arme trouvée dans la catégorie "${selectedCategory}"`,
            ephemeral: true
        });
        return;
    }

    const selectedWeapon = getRandomChoice(weapons);
    
    const embed = new EmbedBuilder()
        .setTitle(`🔫 ${selectedCategory}`)
        .setDescription(`Votre arme principale aléatoire :`)
        .setColor(0x00ff00)
        .setTimestamp()
        .addFields({
            name: '🎯 Arme sélectionnée',
            value: `\`\`\`${selectedWeapon}\`\`\``,
            inline: false
        })
        .setFooter({ text: '🍀 Bonne chance !' });

    await interaction.update({ embeds: [embed], components: [] });
}