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

    # Fonction helper pour supprimer un message de manière sûre et non-bloquante
    async def safe_delete_message(message, message_dict, channel_id):
        try:
            await message.delete()
            message_dict.pop(channel_id, None)
        except (discord.NotFound, discord.Forbidden):
            message_dict.pop(channel_id, None)

    # Fonction helper optimisée pour supprimer l'ancien message
    async def delete_last_message(channel_id, message_dict):
        if channel_id in message_dict:
            old_message = message_dict.get(channel_id)
            if old_message:
                bot.loop.create_task(safe_delete_message(old_message, message_dict, channel_id))

    # Commandes
    @bot.tree.command(name="roll", description="🎲 Génère une classe aléatoire complète")
    async def slash_roll(interaction: discord.Interaction):
        # Réponse immédiate sans defer pour éviter les problèmes d'expiration
        update_stats("roll_slash")
        
        # Génération immédiate
        classe = generer_classe()
        embed = create_class_embed(classe)
        view = RollView(classe)
        
        # Supprime l'ancien message en arrière-plan (non bloquant)
        channel_id = interaction.channel_id
        if channel_id in last_roll_messages:
            old_message = last_roll_messages.get(channel_id)
            # Ne pas attendre la suppression pour éviter les délais
            if old_message:
                bot.loop.create_task(safe_delete_message(old_message, last_roll_messages, channel_id))
        
        # Réponse directe et immédiate
        try:
            await interaction.response.send_message(embed=embed, view=view)
            # Stocke la référence du nouveau message
            message = await interaction.original_response()
            last_roll_messages[channel_id] = message
        except (discord.errors.NotFound, discord.errors.InteractionResponded) as e:
            # L'interaction a expiré, mais on continue sans erreur
            pass

    @bot.tree.command(name="principale", description="🔫 Choisir une arme principale par catégorie")
    async def slash_principale(interaction: discord.Interaction):
        update_stats("principale")
        
        # Supprime l'ancien message en arrière-plan
        channel_id = interaction.channel_id
        await delete_last_message(channel_id, last_principale_messages)
        
        view = PrincipaleView()
        embed = discord.Embed(
            title="🔫 Armes principales",
            description="Choisissez une catégorie pour obtenir une arme aléatoire dedans.",
            color=0x00ccff,
            timestamp=datetime.now()
        )
        
        try:
            await interaction.response.send_message(embed=embed, view=view)
            # Stocke la référence du nouveau message
            message = await interaction.original_response()
            last_principale_messages[channel_id] = message
        except (discord.errors.NotFound, discord.errors.InteractionResponded):
            pass

    @bot.tree.command(name="secondaire", description="🗡️ Choisir une arme secondaire par catégorie")
    async def slash_secondaire(interaction: discord.Interaction):
        update_stats("secondaire")
        
        # Supprime l'ancien message en arrière-plan
        channel_id = interaction.channel_id
        await delete_last_message(channel_id, last_secondaire_messages)
        
        view = SecondaireView()
        embed = discord.Embed(
            title="🗡️ Armes secondaires",
            description="Choisissez une catégorie (Pistolets, Lanceurs ou Spécial) pour obtenir une arme aléatoire dedans.",
            color=0x00ccff,
            timestamp=datetime.now()
        )
        
        try:
            await interaction.response.send_message(embed=embed, view=view)
            # Stocke la référence du nouveau message
            message = await interaction.original_response()
            last_secondaire_messages[channel_id] = message
        except (discord.errors.NotFound, discord.errors.InteractionResponded):
            pass

    @bot.tree.command(name="défis", description="🏆 Choisir un défi aléatoire")
    async def slash_defis(interaction: discord.Interaction):
        update_stats("defis")
        from views.defiView import DefiView, create_defi_embed
        
        # Supprime l'ancien message en arrière-plan
        channel_id = interaction.channel_id
        await delete_last_message(channel_id, last_defi_messages)
        
        view = DefiView()
        embed = create_defi_embed()
        
        try:
            await interaction.response.send_message(embed=embed, view=view)
            # Stocke la référence du nouveau message
            message = await interaction.original_response()
            last_defi_messages[channel_id] = message
        except (discord.errors.NotFound, discord.errors.InteractionResponded):
            pass

    @bot.tree.command(name="aide", description="📖 Affiche l'aide du bot BO6")
    async def slash_aide(interaction: discord.Interaction):
        await interaction.response.defer()
        
        # Supprime le dernier message d'aide dans ce canal s'il existe
        channel_id = interaction.channel_id
        await delete_last_message(channel_id, last_aide_messages)
        
        from views.aideView import AideView, create_aide_embed
        view = AideView()
        embed = create_aide_embed()
        
        await interaction.followup.send(embed=embed, view=view)
        # Stocke la référence du nouveau message
        message = await interaction.original_response()
        last_aide_messages[channel_id] = message

    @bot.tree.command(name="sync", description="🔄 Synchronise les commandes du bot")
    @commands.is_owner()  # Seul le propriétaire du bot peut utiliser cette commande
    async def sync(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        try:
            synced = await bot.tree.sync()
            await interaction.followup.send(f"✅ {len(synced)} commandes synchronisées !", ephemeral=True)
        except Exception as e:
            await interaction.followup.send(f"❌ Erreur lors de la synchronisation : {str(e)}", ephemeral=True)

    from views import DeleteConfirmView

    @bot.tree.command(name="delete", description="🧹 Supprime tous les messages du bot dans ce salon")
    async def slash_delete(interaction: discord.Interaction):
        # Réponse immédiate pour éviter l'expiration de l'interaction
        await interaction.response.defer(ephemeral=True)
        
        view = DeleteConfirmView(bot)
        await interaction.followup.send(
            "⚠️ **Voulez-vous supprimer tous les messages du bot dans ce salon ?**\n\n*Cette action ne peut pas être annulée.*",
            view=view,
            ephemeral=True
        )