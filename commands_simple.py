from discord.ext import commands
import discord
from datetime import datetime
from utils.stats import update_stats
from utils.classGenerator import generer_classe
from views.principaleView import PrincipaleView
from views.secondaireView import SecondaireView
from views.rollView import RollView, create_class_embed
from views import DeleteConfirmView

async def setup(bot):
    # Variables pour stocker le dernier message de chaque commande par canal
    last_roll_messages = {}
    last_principale_messages = {}
    last_secondaire_messages = {}
    last_defi_messages = {}
    last_aide_messages = {}

    @bot.tree.command(name="roll", description="🎲 Génère une classe aléatoire complète")
    async def slash_roll(interaction: discord.Interaction):
        update_stats("roll_slash")
        
        # Génération immédiate
        classe = generer_classe()
        embed = create_class_embed(classe)
        view = RollView(classe)
        
        # Supprime l'ancien message si il existe (en arrière plan)
        channel_id = interaction.channel_id
        if channel_id in last_roll_messages:
            old_message = last_roll_messages.get(channel_id)
            if old_message:
                try:
                    await old_message.delete()
                except:
                    pass
        
        # Réponse directe
        await interaction.response.send_message(embed=embed, view=view)
        
        # Stocke la référence du nouveau message
        message = await interaction.original_response()
        last_roll_messages[channel_id] = message

    @bot.tree.command(name="principale", description="🔫 Choisir une arme principale par catégorie")
    async def slash_principale(interaction: discord.Interaction):
        update_stats("principale")
        
        view = PrincipaleView()
        embed = discord.Embed(
            title="🔫 Armes principales",
            description="Choisissez une catégorie pour obtenir une arme aléatoire dedans.",
            color=0x00ccff,
            timestamp=datetime.now()
        )
        
        await interaction.response.send_message(embed=embed, view=view)

    @bot.tree.command(name="secondaire", description="🗡️ Choisir une arme secondaire par catégorie")
    async def slash_secondaire(interaction: discord.Interaction):
        update_stats("secondaire")
        
        view = SecondaireView()
        embed = discord.Embed(
            title="🗡️ Armes secondaires",
            description="Choisissez une catégorie (Pistolets, Lanceurs ou Spécial) pour obtenir une arme aléatoire dedans.",
            color=0x00ccff,
            timestamp=datetime.now()
        )
        
        await interaction.response.send_message(embed=embed, view=view)

    @bot.tree.command(name="défis", description="🏆 Choisir un défi aléatoire")
    async def slash_defis(interaction: discord.Interaction):
        update_stats("defis")
        from views.defiView import DefiView, create_defi_embed
        
        view = DefiView()
        embed = create_defi_embed()
        
        await interaction.response.send_message(embed=embed, view=view)

    @bot.tree.command(name="aide", description="📖 Affiche l'aide du bot BO6")
    async def slash_aide(interaction: discord.Interaction):
        from views.aideView import AideView, create_aide_embed
        view = AideView()
        embed = create_aide_embed()
        
        await interaction.response.send_message(embed=embed, view=view)

    @bot.tree.command(name="sync", description="🔄 Synchronise les commandes du bot")
    @commands.is_owner()
    async def sync(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        try:
            synced = await bot.tree.sync()
            await interaction.followup.send(f"✅ {len(synced)} commandes synchronisées !", ephemeral=True)
        except Exception as e:
            await interaction.followup.send(f"❌ Erreur lors de la synchronisation : {str(e)}", ephemeral=True)

    @bot.tree.command(name="delete", description="🧹 Supprime tous les messages du bot dans ce salon")
    async def slash_delete(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        view = DeleteConfirmView(bot)
        await interaction.followup.send(
            "⚠️ **Voulez-vous supprimer tous les messages du bot dans ce salon ?**\n\n*Cette action ne peut pas être annulée.*",
            view=view,
            ephemeral=True
        )
