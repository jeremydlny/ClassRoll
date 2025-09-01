import discord
from datetime import datetime
from utils.classGenerator import generer_classe, generer_arme_aleatoire
from utils.stats import update_stats
from views.armeView import ArmeView
from views.defiView import DefiView

class RollView(discord.ui.View):
    def __init__(self, classe):
        super().__init__(timeout=300)
        self.classe = classe

    @discord.ui.button(label='🔄 RE-ROLL', style=discord.ButtonStyle.primary)
    async def reroll(self, interaction: discord.Interaction, button: discord.ui.Button):
        update_stats("reroll")
        nouvelle_classe = generer_classe()
        self.classe = nouvelle_classe
        embed = create_class_embed(nouvelle_classe)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label='🎯 ARME SEULE', style=discord.ButtonStyle.success)
    async def arme_seule(self, interaction: discord.Interaction, button: discord.ui.Button):
        arme = generer_arme_aleatoire()
        embed = discord.Embed(title="🎯 Arme Aléatoire", color=0x0099ff, timestamp=datetime.now())
        embed.add_field(name="🔫 Votre arme", value=f"```{arme}```", inline=False)
        embed.set_footer(text="🍀 Bonne chance !")
        await interaction.response.edit_message(embed=embed, view=ArmeView(self.classe))

    @discord.ui.button(label='🏆 DÉFI', style=discord.ButtonStyle.danger)
    async def defi(self, interaction: discord.Interaction, button: discord.ui.Button):
        from utils.classGenerator import defis_data
        view = DefiView(self.classe)
        embed = discord.Embed(
            title="🏆 Choisissez votre défi !",
            description="Sélectionnez le niveau de difficulté :",
            color=0xff4444,
            timestamp=datetime.now()
        )
        for niveau, defis_list in defis_data.items():
            if isinstance(defis_list, list):
                embed.add_field(
                    name=f"{niveau.title()}",
                    value=f"```{len(defis_list)} défis disponibles```",
                    inline=True
                )
        await interaction.response.edit_message(embed=embed, view=view)

def create_class_embed(classe):
    """Créer un embed Discord pour afficher la classe générée"""
    embed = discord.Embed(title="🎲 Classe Générée", color=0x0099ff, timestamp=datetime.now())
    embed.add_field(name="🔫 Arme n°1", value=f"```{classe['arme_principale']}```", inline=True)
    embed.add_field(name="🔫 Arme n°2", value=f"```{classe['arme_secondaire']}```", inline=True)
    embed.add_field(name="", value="", inline=True)  # Spacer
    embed.add_field(name="⚡ Atout 1", value=f"```{classe['atout_1']}```", inline=True)
    embed.add_field(name="⚡ Atout 2", value=f"```{classe['atout_2']}```", inline=True)
    embed.add_field(name="⚡ Atout 3", value=f"```{classe['atout_3']}```", inline=True)
    embed.add_field(name="🎯 Équipement tactique", value=f"```{classe['equipement_tactique']}```", inline=True)
    embed.add_field(name="💥 Équipement mortel", value=f"```{classe['equipement_mortel']}```", inline=True)
    embed.add_field(name="", value="", inline=True)  # Spacer
    embed.set_footer(text="🍀 Bonne chance!")
    return embed
