import { ActionRowBuilder, ButtonBuilder, ButtonStyle, EmbedBuilder } from 'discord.js';
import { generateClass, generateRandomWeapon } from '../utils/classGenerator.js';
import { updateStats } from '../utils/stats.js';

/**
 * Create an embed for displaying a generated class
 * @param {Object} classe - The generated class object
 * @returns {EmbedBuilder} Discord embed
 */
export function createClassEmbed(classe) {
    const embed = new EmbedBuilder()
        .setTitle('🎲 Classe Générée')
        .setColor(0x0099ff)
        .setTimestamp()
        .addFields(
            { name: '🔫 Arme n°1', value: `\`\`\`${classe.arme_principale}\`\`\``, inline: true },
            { name: '🔫 Arme n°2', value: `\`\`\`${classe.arme_secondaire}\`\`\``, inline: true },
            { name: '', value: '', inline: true }, // Spacer
            { name: '⚡ Atout 1', value: `\`\`\`${classe.atout_1}\`\`\``, inline: true },
            { name: '⚡ Atout 2', value: `\`\`\`${classe.atout_2}\`\`\``, inline: true },
            { name: '⚡ Atout 3', value: `\`\`\`${classe.atout_3}\`\`\``, inline: true },
            { name: '🎯 Équipement tactique', value: `\`\`\`${classe.equipement_tactique}\`\`\``, inline: true },
            { name: '💥 Équipement mortel', value: `\`\`\`${classe.equipement_mortel}\`\`\``, inline: true },
            { name: '', value: '', inline: true } // Spacer
        )
        .setFooter({ text: '🍀 Bonne chance!' });
    
    return embed;
}

/**
 * Create the main roll view with all interaction buttons
 * @param {Object} classe - The initial generated class
 * @returns {Object} Components for the message
 */
export function createRollView(classe) {
    const row1 = new ActionRowBuilder()
        .addComponents(
            new ButtonBuilder()
                .setCustomId('reroll')
                .setLabel('🔄 RE-ROLL')
                .setStyle(ButtonStyle.Primary),
            new ButtonBuilder()
                .setCustomId('arme_seule')
                .setLabel('🎯 ARME SEULE')
                .setStyle(ButtonStyle.Success),
            new ButtonBuilder()
                .setCustomId('defi')
                .setLabel('🏆 DÉFI')
                .setStyle(ButtonStyle.Danger)
        );

    const row2 = new ActionRowBuilder()
        .addComponents(
            new ButtonBuilder()
                .setCustomId('arme_principale_direct')
                .setLabel('🔫 ARME PRINCIPALE')
                .setStyle(ButtonStyle.Secondary),
            new ButtonBuilder()
                .setCustomId('arme_secondaire_direct')
                .setLabel('🗡️ ARME SECONDAIRE')
                .setStyle(ButtonStyle.Secondary)
        );

    return { components: [row1, row2] };
}

/**
 * Handle button interactions for the roll view
 * @param {Interaction} interaction - Discord interaction
 * @param {Object} classe - Current class data
 * @returns {Object|null} New class data if changed, null otherwise
 */
export async function handleRollInteraction(interaction, classe) {
    const customId = interaction.customId;

    switch (customId) {
        case 'reroll':
            await interaction.deferUpdate();
            updateStats('reroll');
            const nouvelleClasse = generateClass();
            const embed = createClassEmbed(nouvelleClasse);
            const view = createRollView(nouvelleClasse);
            await interaction.editReply({ embeds: [embed], ...view });
            return nouvelleClasse;

        case 'arme_seule':
            await interaction.deferUpdate();
            const arme = generateRandomWeapon();
            const armeEmbed = new EmbedBuilder()
                .setTitle('🎯 Arme Aléatoire')
                .setColor(0x0099ff)
                .setTimestamp()
                .addFields({ name: '🔫 Votre arme', value: `\`\`\`${arme}\`\`\``, inline: false })
                .setFooter({ text: '🍀 Bonne chance !' });
            
            // Create back button to return to class view
            const armeRow = new ActionRowBuilder()
                .addComponents(
                    new ButtonBuilder()
                        .setCustomId('back_to_class')
                        .setLabel('🔙 Retour à la classe')
                        .setStyle(ButtonStyle.Secondary)
                );
            
            await interaction.editReply({ embeds: [armeEmbed], components: [armeRow] });
            break;

        case 'back_to_class':
            await interaction.deferUpdate();
            const classEmbed = createClassEmbed(classe);
            const classView = createRollView(classe);
            await interaction.editReply({ embeds: [classEmbed], ...classView });
            break;

        case 'defi':
            await interaction.deferUpdate();
            // Import defi view dynamically to avoid circular imports
            const { createDefiView, createDefiEmbed } = await import('./defiView.js');
            const defiEmbed = createDefiEmbed();
            const defiView = createDefiView(classe);
            await interaction.editReply({ embeds: [defiEmbed], ...defiView });
            break;

        case 'arme_principale_direct':
            updateStats('principale');
            const { createPrincipaleEmbed, createPrincipaleView } = await import('./principaleView.js');
            const principaleEmbed = createPrincipaleEmbed();
            const principaleView = createPrincipaleView();
            await interaction.reply({ embeds: [principaleEmbed], ...principaleView });
            break;

        case 'arme_secondaire_direct':
            updateStats('secondaire');
            const { createSecondaireEmbed, createSecondaireView } = await import('./secondaireView.js');
            const secondaireEmbed = createSecondaireEmbed();
            const secondaireView = createSecondaireView();
            await interaction.reply({ embeds: [secondaireEmbed], ...secondaireView });
            break;

        default:
            return null;
    }
    
    return null;
}