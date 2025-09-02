import { Client, GatewayIntentBits, Events } from 'discord.js';
import { config } from 'dotenv';
import { setupCommands, handleSlashCommand } from './commands/index.js';
import { handleRollInteraction } from './views/rollView.js';
import { handlePrincipaleSelection } from './views/principaleView.js';
import { handleSecondaireSelection } from './views/secondaireView.js';
import { handleDefiSelection } from './views/defiView.js';
import { logger } from './utils/logger.js';

// Load environment variables
config();

// Create Discord client with required intents
const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
        GatewayIntentBits.GuildMembers
    ]
});

// Store current class data for button interactions
const classDataStore = new Map();

// Bot ready event
client.once(Events.ClientReady, async (readyClient) => {
    logger.info(`✅ Bot connecté: ${readyClient.user.tag} (ID: ${readyClient.user.id})`);
    
    try {
        await setupCommands(readyClient);
        logger.info('✅ Commandes synchronisées');
    } catch (error) {
        logger.error('❌ Erreur sync commandes: ' + error.message);
    }
});

// Handle slash command interactions
client.on(Events.InteractionCreate, async (interaction) => {
    try {
        if (interaction.isChatInputCommand()) {
            await handleSlashCommand(interaction, classDataStore);
        } else if (interaction.isButton()) {
            // Handle button interactions from roll view
            const userId = interaction.user.id;
            const classe = classDataStore.get(userId) || {};
            
            const newClasse = await handleRollInteraction(interaction, classe);
            
            // Update stored class data if it changed
            if (newClasse) {
                classDataStore.set(userId, newClasse);
            }
        } else if (interaction.isStringSelectMenu()) {
            // Handle select menu interactions
            switch (interaction.customId) {
                case 'select_principale':
                    await handlePrincipaleSelection(interaction);
                    break;
                case 'select_secondaire':
                    await handleSecondaireSelection(interaction);
                    break;
                case 'select_defi':
                    await handleDefiSelection(interaction);
                    break;
            }
        }
    } catch (error) {
        logger.error('Error handling interaction: ' + error.message);
        console.error(error);
        
        // Try to respond with an error message
        const errorMessage = { 
            content: 'Une erreur est survenue lors de l\'exécution de cette action.', 
            ephemeral: true 
        };
        
        try {
            if (interaction.replied || interaction.deferred) {
                await interaction.followUp(errorMessage);
            } else {
                await interaction.reply(errorMessage);
            }
        } catch (replyError) {
            logger.error('Could not send error message: ' + replyError.message);
        }
    }
});

// Error handling
client.on(Events.Error, (error) => {
    logger.error('Client error: ' + error.message);
    console.error(error);
});

client.on(Events.Warn, (warning) => {
    logger.warn('Client warning: ' + warning);
});

// Process error handling
process.on('unhandledRejection', (error) => {
    logger.error('Unhandled promise rejection: ' + error.message);
    console.error(error);
});

process.on('uncaughtException', (error) => {
    logger.error('Uncaught exception: ' + error.message);
    console.error(error);
    process.exit(1);
});

/**
 * Start the Discord bot
 */
async function startBot() {
    const discordToken = process.env.DISCORD_BOT_TOKEN;
    
    if (!discordToken) {
        logger.error('DISCORD_BOT_TOKEN non trouvé dans les variables d\'environnement');
        logger.error('Créez un fichier .env basé sur .env.example');
        process.exit(1);
    }
    
    logger.info('🚀 Démarrage du bot...');
    
    try {
        await client.login(discordToken);
    } catch (error) {
        logger.error('❌ Erreur lors du démarrage du bot: ' + error.message);
        console.error(error);
        process.exit(1);
    }
}

// Start the bot if this file is run directly
if (import.meta.url === `file://${process.argv[1]}`) {
    startBot();
}

export { startBot };