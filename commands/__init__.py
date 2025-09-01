from discord.ext import commands
import discord
from datetime import datetime
from utils.stats import update_stats
from utils.classGenerator import armes_data, safe_list
from views.pick1View import Pick1View
from views.pick2View import Pick2View
from views.rollView import RollView, create_class_embed
from utils.classGenerator import generer_classe

async def setup(bot):
    # Variable pour stocker le dernier message de roll par canal
    last_roll_messages = {}

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

    @bot.tree.command(name="pick1", description="🔫 Choisir une arme principale par catégorie")
    async def slash_pick1(interaction: discord.Interaction):
        update_stats("pick1")
        view = Pick1View()
        embed = discord.Embed(
            title="🔫 PICK 1 — Armes principales",
            description="Choisissez une catégorie pour obtenir une arme aléatoire dedans.",
            color=0x00ccff,
            timestamp=datetime.now()
        )
        await interaction.response.send_message(embed=embed, view=view)

    @bot.tree.command(name="pick2", description="🗡️ Choisir une arme secondaire par catégorie")
    async def slash_pick2(interaction: discord.Interaction):
        update_stats("pick2")
        view = Pick2View()
        embed = discord.Embed(
            title="🗡️ PICK 2 — Armes secondaires",
            description="Choisissez une catégorie (Pistolets, Lanceurs ou Spécial) pour obtenir une arme aléatoire dedans.",
            color=0x00ccff,
            timestamp=datetime.now()
        )
        await interaction.response.send_message(embed=embed, view=view)

    @bot.tree.command(name="aide", description="📖 Affiche l'aide du bot BO6")
    async def slash_aide(interaction: discord.Interaction):
        embed = discord.Embed(title="📖 Aide - WeaponRoll", color=0x0099ff, timestamp=datetime.now())
        embed.add_field(
            name="🎲 /roll",
            value=(
                "Génère une classe BO6 complète avec :\n"
                f"- {len(safe_list(armes_data,'principales'))} armes principales\n"
                f"- {len(safe_list(armes_data,'secondaires'))} armes secondaires\n"
                "- 3 atouts (1 par slot) si définis dans atouts.json\n"
                "- Équipements (tactiques & mortels)\n"
                "- Boutons : RE-ROLL, ARME SEULE, DÉFI"
            ),
            inline=False
        )
        embed.add_field(
            name="🎯 /pick1",
            value=(
                "Ouvre une interface pour choisir une arme principale aléatoire parmi les catégories :\n"
                "- Fusils d'assaut\n"
                "- Mitraillettes\n"
                "- Fusils à pompe\n"
                "- Mitrailleuses\n"
                "- Fusils tactiques\n"
                "- Fusils de précision"
            ),
            inline=False
        )
        embed.add_field(
            name="🗡️ /pick2",
            value=(
                "Ouvre une interface pour choisir une arme secondaire aléatoire parmi les catégories :\n"
                "- **Pistolets**\n"
                "- **Lanceurs**\n"
                "- **Spécial**"
            ),
            inline=False
        )
        embed.add_field(
            name="🎯 Commandes de défi",
            value=(
                "Utilisez **!theme meta** pour des armes méta\n"
                "Utilisez **!defi_equipe rouge** pour handicaper une équipe\n"
                "Utilisez **!win bleu** pour victoire avec defi auto"
            ),
            inline=False
        )
        embed.set_footer(text="PPBot • Bot pour Resurgence/PartyPlay")
        await interaction.response.send_message(embed=embed)
