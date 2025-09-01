import discord
from datetime import datetime
from utils.classGenerator import armes_data

class AideView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)

def create_aide_embed():
    embed = discord.Embed(title="📖 Aide - WeaponRoll", color=0x0099ff, timestamp=datetime.now())
    embed.add_field(
        name="🎲 /roll",
        value=(
            "Génère une classe BO6 complète avec :\n"
            f"- {sum(len(armes) for armes in armes_data.get('principales', {}).values())} armes principales\n"
            f"- {sum(len(armes) for armes in armes_data.get('secondaires', {}).values())} armes secondaires\n"
            "- 3 atouts (1 par slot) si définis dans atouts.json\n"
            "- Équipements (tactiques & mortels)\n"
            "- Boutons : RE-ROLL, ARME SEULE, DÉFI"
        ),
        inline=False
    )
    embed.add_field(
        name="🔫 /principale",
        value=(
            "Ouvre une interface pour choisir une arme principale aléatoire parmi les catégories :\n"
            "- **Fusils d'assaut**\n"
            "- **Mitraillettes**\n"
            "- **Fusils à pompe**\n"
            "- **Mitrailleuses**\n"
            "- **Fusils tactiques**\n"
            "- **Fusils de précision**"
        ),
        inline=False
    )
    embed.add_field(
        name="🗡️ /secondaire",
        value=(
            "Ouvre une interface pour choisir une arme secondaire aléatoire parmi les catégories :\n"
            "- **Pistolets**\n"
            "- **Lanceurs**\n"
            "- **Spécial**"
        ),
        inline=False
    )
    embed.add_field(
        name="🏆 /défis",
        value=(
            "Ouvre une interface pour choisir un défi aléatoire par niveau de difficulté :\n"
            "- 🟢 **Facile**\n"
            "- 🟡 **Moyen**\n"
            "- 🔴 **Difficile**"
        ),
        inline=False
    )
    return embed
