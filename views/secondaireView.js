import { ActionRowBuilder, StringSelectMenuBuilder, EmbedBuilder } from 'discord.js';
import { findCategoryList } from '../utils/classGenerator.js';
import { getRandomChoice } from '../utils/random.js';

/**
 * Create embed for secondary weapons selection
 * @returns {EmbedBuilder} Discord embed
 */
export function createSecondaireEmbed() {
    return new EmbedBuilder()
        .setTitle('🗡️ Armes secondaires')
        .setDescription('```Choisissez une catégorie (Pistolets, Lanceurs ou Spécial) pour obtenir une arme aléatoire dedans.```')
        .setColor(0x00ccff)
        .setTimestamp();
}

/**
 * Create the secondary weapons selection view
 * @returns {Object} Components for the message
 */
export function createSecondaireView() {
    const selectMenu = new StringSelectMenuBuilder()
        .setCustomId('select_secondaire')
        .setPlaceholder('Choisissez une catégorie d\'arme secondaire')
        .addOptions([
            {
                label: 'Pistolets',
                description: 'Armes de poing classiques',
                value: 'Pistolets',
                emoji: '🔫'
            },
            {
                label: 'Lanceurs',
                description: 'Lance-roquettes et explosifs',
                value: 'Lanceurs',
                emoji: '🚀'
            },
            {
                label: 'Spécial',
                description: 'Armes spéciales et uniques',
                value: 'Spécial',
                emoji: '⭐'
            }
        ]);

    const row = new ActionRowBuilder()
        .addComponents(selectMenu);

    return { components: [row] };
}

/**
 * Handle secondary weapon selection interaction
 * @param {Interaction} interaction - Discord interaction
 */
export async function handleSecondaireSelection(interaction) {
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
        .setTitle(`🗡️ ${selectedCategory}`)
        .setDescription(`Votre arme secondaire aléatoire :`)
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