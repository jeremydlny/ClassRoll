import discord
from datetime import datetime
import random
from utils.classGenerator import defis_data, safe_list

def create_defi_embed():
    """Crée l'embed initial pour la sélection des défis"""
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
    embed.set_footer(text="🍀 Bonne chance!")
    return embed

class DefiView(discord.ui.View):
    def __init__(self, classe=None):
        super().__init__(timeout=300)
        self.classe = classe

    @discord.ui.button(label="↩️ Retour", style=discord.ButtonStyle.secondary, row=1)
    async def retour(self, interaction: discord.Interaction, button: discord.ui.Button):
        from views.rollView import RollView, create_class_embed
        from utils.classGenerator import generer_classe
        classe = generer_classe()
        embed = create_class_embed(classe)
        view = RollView(classe)
        await interaction.response.edit_message(embed=embed, view=view)

    @discord.ui.button(label='🟢 Facile', style=discord.ButtonStyle.success, row=0)
    async def facile(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        defis_faciles = safe_list(defis_data, 'facile')
        if not defis_faciles:
            await interaction.followup.send("❌ Aucun défi facile disponible", ephemeral=True)
            return
        
        defi = random.choice(defis_faciles)
        embed = discord.Embed(title="🟢 Défi Facile", color=0x00ff00, timestamp=datetime.now())
        embed.add_field(name="🎯 Votre défi", value=f"```{defi}```", inline=False)
        embed.set_footer(text="🍀 Relevez le défi !")
        await interaction.edit_original_response(embed=embed, view=self)

    @discord.ui.button(label='🟡 Moyen', style=discord.ButtonStyle.primary)
    async def moyen(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        defis_moyens = safe_list(defis_data, 'moyen')
        if not defis_moyens:
            await interaction.followup.send("❌ Aucun défi moyen disponible", ephemeral=True)
            return
        
        defi = random.choice(defis_moyens)
        embed = discord.Embed(title="🟡 Défi Moyen", color=0xffff00, timestamp=datetime.now())
        embed.add_field(name="🎯 Votre défi", value=f"```{defi}```", inline=False)
        embed.set_footer(text="🍀 Relevez le défi !")
        await interaction.edit_original_response(embed=embed, view=self)

    @discord.ui.button(label='🔴 Difficile', style=discord.ButtonStyle.danger)
    async def difficile(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        defis_difficiles = safe_list(defis_data, 'difficile')
        if not defis_difficiles:
            await interaction.followup.send("❌ Aucun défi difficile disponible", ephemeral=True)
            return
        
        defi = random.choice(defis_difficiles)
        embed = discord.Embed(title="🔴 Défi Difficile", color=0xff0000, timestamp=datetime.now())
        embed.add_field(name="🎯 Votre défi", value=f"```{defi}```", inline=False)
        embed.set_footer(text="🍀 Relevez le défi !")
        await interaction.edit_original_response(embed=embed, view=self)
        
    @discord.ui.button(label='↩️ RETOUR', style=discord.ButtonStyle.secondary, row=1)
    async def retour(self, interaction: discord.Interaction, button: discord.ui.Button):
        from views.rollView import RollView, create_class_embed
        if self.classe:
            view = RollView(self.classe)
            embed = create_class_embed(self.classe)
            await interaction.response.edit_message(embed=embed, view=view)
        else:
            # Si pas de classe sauvegardée, en générer une nouvelle
            from utils.classGenerator import generer_classe
            nouvelle_classe = generer_classe()
            view = RollView(nouvelle_classe)
            embed = create_class_embed(nouvelle_classe)
            await interaction.response.edit_message(embed=embed, view=view)
