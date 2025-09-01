import discord
from datetime import datetime
from utils.classGenerator import find_category_list
import random

class PrincipaleView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)

    @discord.ui.button(label="Fusils d'assaut", style=discord.ButtonStyle.primary, row=0)
    async def fusils_assaut(self, interaction: discord.Interaction, button: discord.ui.Button):
        armes = find_category_list("Fusils d'assaut")
        if not armes:
            return await interaction.response.send_message("❌ Aucune arme dans cette catégorie", ephemeral=True)
        arme = random.choice(armes)
        embed = discord.Embed(title="🔫 Principale — Fusils d'assaut", description=f"```{arme}```", color=0x00ccff, timestamp=datetime.now())
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Mitraillettes", style=discord.ButtonStyle.primary, row=0)
    async def mitraillettes(self, interaction: discord.Interaction, button: discord.ui.Button):
        armes = find_category_list("Mitraillettes")
        if not armes:
            return await interaction.response.send_message("❌ Aucune arme dans cette catégorie", ephemeral=True)
        arme = random.choice(armes)
        embed = discord.Embed(title="🔫 Principale — Mitraillettes", description=f"```{arme}``", color=0x00ccff, timestamp=datetime.now())
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Fusils à pompe", style=discord.ButtonStyle.primary, row=1)
    async def fusils_pompe(self, interaction: discord.Interaction, button: discord.ui.Button):
        armes = find_category_list("Fusils à pompe")
        if not armes:
            return await interaction.response.send_message("❌ Aucune arme dans cette catégorie", ephemeral=True)
        arme = random.choice(armes)
        embed = discord.Embed(title="🔫 Principale — Fusils à pompe", description=f"```{arme}``", color=0x00ccff, timestamp=datetime.now())
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Mitrailleuses", style=discord.ButtonStyle.primary, row=1)
    async def mitrailleuses(self, interaction: discord.Interaction, button: discord.ui.Button):
        armes = find_category_list("Mitrailleuses")
        if not armes:
            return await interaction.response.send_message("❌ Aucune arme dans cette catégorie", ephemeral=True)
        arme = random.choice(armes)
        embed = discord.Embed(title="🔫 Principale — Mitrailleuses", description=f"```{arme}``", color=0x00ccff, timestamp=datetime.now())
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Fusils tactiques", style=discord.ButtonStyle.primary, row=2)
    async def fusils_tactiques(self, interaction: discord.Interaction, button: discord.ui.Button):
        armes = find_category_list("Fusils tactiques")
        if not armes:
            return await interaction.response.send_message("❌ Aucune arme dans cette catégorie", ephemeral=True)
        arme = random.choice(armes)
        embed = discord.Embed(title="🔫 Principale — Fusils tactiques", description=f"```{arme}``", color=0x00ccff, timestamp=datetime.now())
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Fusils de précision", style=discord.ButtonStyle.primary, row=2)
    async def fusils_precision(self, interaction: discord.Interaction, button: discord.ui.Button):
        armes = find_category_list("Fusils de précision")
        if not armes:
            return await interaction.response.send_message("❌ Aucune arme dans cette catégorie", ephemeral=True)
        arme = random.choice(armes)
        embed = discord.Embed(title="🔫 Principale — Fusils de précision", description=f"```{arme}``", color=0x00ccff, timestamp=datetime.now())
        await interaction.response.edit_message(embed=embed, view=self)
