from discord.ext import commands
import discord
from datetime import datetime
from utils.stats import update_stats
from utils.classGenerator import armes_data, safe_list
from views.principaleView import PrincipaleView
from views.secondaireView import SecondaireView
from views.rollView import RollView, create_class_embed
from utils.classGenerator import generer_classe

async def setup(bot):
    # Variables pour stocker le dernier message de chaque commande par canal
    last_roll_messages = {}
    last_principale_messages = {}
    last_secondaire_messages = {}
    last_defi_messages = {}
    last_aide_messages = {}

    # Fonction helper pour supprimer l'ancien message
    async def delete_last_message(channel_id, message_dict):
        if channel_id in message_dict:
            try:
                last_message = message_dict[channel_id]
                await last_message.delete()
            except (discord.NotFound, discord.Forbidden):
                pass  # Message déjà supprimé ou pas les permissions

    # Commandes
    @bot.tree.command(name="roll", description="🎲 Génère une classe aléatoire complète")
    async def slash_roll(interaction: discord.Interaction):
        update_stats("roll_slash")
        
        # Supprime le dernier message de roll dans ce canal s'il existe
        channel_id = interaction.channel_id
        if channel_id in last_roll_messages:
            try:
                last_message = last_roll_messages[channel_id]
                await last_message.delete()
            except (discord.NotFound, discord.Forbidden):
                pass  # Message déjà supprimé ou pas les permissions
        
        # Envoie le nouveau message
        classe = generer_classe()
        embed = create_class_embed(classe)
        view = RollView(classe)
        
        # Envoie le message et stocke la référence
        await interaction.response.send_message(embed=embed, view=view)
        # Obtient le message envoyé
        message = await interaction.original_response()
        last_roll_messages[channel_id] = message

    @bot.tree.command(name="principale", description="🔫 Choisir une arme principale par catégorie")
    async def slash_principale(interaction: discord.Interaction):
        update_stats("principale")
        
        # Supprime le dernier message de principale dans ce canal s'il existe
        channel_id = interaction.channel_id
        await delete_last_message(channel_id, last_principale_messages)
        
        view = PrincipaleView()
        embed = discord.Embed(
            title="🔫 Armes principales",
            description="Choisissez une catégorie pour obtenir une arme aléatoire dedans.",
            color=0x00ccff,
            timestamp=datetime.now()
        )
        await interaction.response.send_message(embed=embed, view=view)
        # Stocke la référence du nouveau message
        message = await interaction.original_response()
        last_principale_messages[channel_id] = message

    @bot.tree.command(name="secondaire", description="🗡️ Choisir une arme secondaire par catégorie")
    async def slash_secondaire(interaction: discord.Interaction):
        update_stats("secondaire")
        
        # Supprime le dernier message de secondaire dans ce canal s'il existe
        channel_id = interaction.channel_id
        await delete_last_message(channel_id, last_secondaire_messages)
        
        view = SecondaireView()
        embed = discord.Embed(
            title="🗡️ Armes secondaires",
            description="Choisissez une catégorie (Pistolets, Lanceurs ou Spécial) pour obtenir une arme aléatoire dedans.",
            color=0x00ccff,
            timestamp=datetime.now()
        )
        await interaction.response.send_message(embed=embed, view=view)
        # Stocke la référence du nouveau message
        message = await interaction.original_response()
        last_secondaire_messages[channel_id] = message

    @bot.tree.command(name="défis", description="🏆 Choisir un défi aléatoire")
    async def slash_defis(interaction: discord.Interaction):
        update_stats("defis")
        from views.defiView import DefiView, create_defi_embed
        
        # Supprime le dernier message de défi dans ce canal s'il existe
        channel_id = interaction.channel_id
        await delete_last_message(channel_id, last_defi_messages)
        
        view = DefiView()
        embed = create_defi_embed()
        
        await interaction.response.send_message(embed=embed, view=view)
        # Stocke la référence du nouveau message
        message = await interaction.original_response()
        last_defi_messages[channel_id] = message

    @bot.tree.command(name="aide", description="📖 Affiche l'aide du bot BO6")
    async def slash_aide(interaction: discord.Interaction):
        # Supprime le dernier message d'aide dans ce canal s'il existe
        channel_id = interaction.channel_id
        await delete_last_message(channel_id, last_aide_messages)
        
        from views.aideView import AideView, create_aide_embed
        view = AideView()
        embed = create_aide_embed()
        
        await interaction.response.send_message(embed=embed, view=view)
        # Stocke la référence du nouveau message
        message = await interaction.original_response()
        last_aide_messages[channel_id] = message

    @bot.tree.command(name="sync", description="🔄 Synchronise les commandes du bot")
    @commands.is_owner()  # Seul le propriétaire du bot peut utiliser cette commande
    async def sync(interaction: discord.Interaction):
        try:
            synced = await bot.tree.sync()
            await interaction.response.send_message(f"✅ {len(synced)} commandes synchronisées !", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ Erreur lors de la synchronisation : {str(e)}", ephemeral=True)
