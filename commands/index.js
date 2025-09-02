import { SlashCommandBuilder } from 'discord.js';
import { updateStats } from '../utils/stats.js';
import { generateClass } from '../utils/classGenerator.js';
import { createClassEmbed, createRollView } from '../views/rollView.js';
import { createPrincipaleEmbed, createPrincipaleView } from '../views/principaleView.js';
import { createSecondaireEmbed, createSecondaireView } from '../views/secondaireView.js';
import { createDefiEmbed, createDefiView } from '../views/defiView.js';
import { createAideEmbed, createAideView } from '../views/aideView.js';

/**
 * Set up all slash commands for the bot
 * @param {Client} client - Discord client instance
 */
export async function setupCommands(client) {
    const commands = [
        new SlashCommandBuilder()
            .setName('roll')
            .setDescription('🎲 Génère une classe aléatoire complète'),
        
        new SlashCommandBuilder()
            .setName('principale')
            .setDescription('🔫 Choisir une arme principale par catégorie'),
        
        new SlashCommandBuilder()
            .setName('secondaire')
            .setDescription('🗡️ Choisir une arme secondaire par catégorie'),
        
        new SlashCommandBuilder()
            .setName('défis')
            .setDescription('🏆 Choisir un défi aléatoire'),
        
        new SlashCommandBuilder()
            .setName('aide')
            .setDescription('📖 Affiche l\'aide du bot BO6'),
        
        new SlashCommandBuilder()
            .setName('sync')
            .setDescription('🔄 Synchronise les commandes du bot'),
        
        new SlashCommandBuilder()
            .setName('delete')
            .setDescription('🧹 Supprime tous les messages du bot dans ce salon')
    ];

    try {
        console.log('Started refreshing application (/) commands.');
        await client.application.commands.set(commands);
        console.log('Successfully reloaded application (/) commands.');
    } catch (error) {
        console.error('Error setting up commands:', error);
    }
}

/**
 * Handle slash command interactions
 * @param {Interaction} interaction - Discord interaction
 * @param {Map} classDataStore - Store for class data per user
 */
export async function handleSlashCommand(interaction, classDataStore = null) {
    if (!interaction.isChatInputCommand()) return;

    const { commandName } = interaction;

    try {
        switch (commandName) {
            case 'roll':
                updateStats('roll_slash');
                const classe = generateClass();
                const embed = createClassEmbed(classe);
                const view = createRollView(classe);
                await interaction.reply({ embeds: [embed], ...view });
                
                // Store class data for button interactions
                if (classDataStore) {
                    classDataStore.set(interaction.user.id, classe);
                }
                break;

            case 'principale':
                updateStats('principale');
                const principaleEmbed = createPrincipaleEmbed();
                const principaleView = createPrincipaleView();
                await interaction.reply({ embeds: [principaleEmbed], ...principaleView });
                break;

            case 'secondaire':
                updateStats('secondaire');
                const secondaireEmbed = createSecondaireEmbed();
                const secondaireView = createSecondaireView();
                await interaction.reply({ embeds: [secondaireEmbed], ...secondaireView });
                break;

            case 'défis':
                updateStats('defis');
                const defiEmbed = createDefiEmbed();
                const defiView = createDefiView();
                await interaction.reply({ embeds: [defiEmbed], ...defiView });
                break;

            case 'aide':
                const aideEmbed = createAideEmbed();
                const aideView = createAideView();
                await interaction.reply({ embeds: [aideEmbed], ...aideView });
                break;

            case 'sync':
                // Check if user is bot owner (you might want to implement proper permission checking)
                await interaction.deferReply({ ephemeral: true });
                try {
                    await setupCommands(interaction.client);
                    await interaction.followUp({ content: '✅ Commandes synchronisées !', ephemeral: true });
                } catch (error) {
                    await interaction.followUp({ 
                        content: `❌ Erreur lors de la synchronisation : ${error.message}`, 
                        ephemeral: true 
                    });
                }
                break;

            case 'delete':
                await interaction.deferReply({ ephemeral: true });
                const channel = interaction.channel;
                let deletedCount = 0;

                try {
                    const messages = await channel.messages.fetch({ limit: 100 });
                    const botMessages = messages.filter(message => message.author.id === interaction.client.user.id);
                    
                    for (const message of botMessages.values()) {
                        try {
                            await message.delete();
                            deletedCount++;
                        } catch (error) {
                            // Message already deleted or no permissions
                            console.log('Could not delete message:', error.message);
                        }
                    }

                    await interaction.followUp({
                        content: `✅ **${deletedCount} message(s) supprimé(s) !**`,
                        ephemeral: true
                    });
                } catch (error) {
                    await interaction.followUp({
                        content: `❌ **Erreur lors de la suppression :** ${error.message}`,
                        ephemeral: true
                    });
                }
                break;

            default:
                await interaction.reply({ 
                    content: 'Commande non reconnue.', 
                    ephemeral: true 
                });
        }
    } catch (error) {
        console.error('Error handling slash command:', error);
        const errorMessage = { 
            content: 'Une erreur est survenue lors de l\'exécution de la commande.', 
            ephemeral: true 
        };
        
        if (interaction.replied || interaction.deferred) {
            await interaction.followUp(errorMessage);
        } else {
            await interaction.reply(errorMessage);
        }
    }
}