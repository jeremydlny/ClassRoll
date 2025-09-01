import discord
from datetime import datetime
from utils.classGenerator import find_category_list
import random

class Pick2View(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)

    @discord.ui.button(label="Pistolets", style=discord.ButtonStyle.primary, row=0)
    async def pistolets(self, interaction: discord.Interaction, button: discord.ui.Button):
        armes = find_category_list("Pistolets")
        if not armes:
            return await interaction.response.send_message("❌ Aucune arme dans cette catégorie", ephemeral=True)
        arme = random.choice(armes)
        embed = discord.Embed(title="🗡️ PICK 2 — Pistolets", description=f"**{arme}**", color=0x00ccff, timestamp=datetime.now())
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Lanceurs", style=discord.ButtonStyle.primary, row=0)
    async def lanceurs(self, interaction: discord.Interaction, button: discord.ui.Button):
        armes = find_category_list("Lanceurs")
        if not armes:
            return await interaction.response.send_message("❌ Aucune arme dans cette catégorie", ephemeral=True)
        arme = random.choice(armes)
        embed = discord.Embed(title="🗡️ PICK 2 — Lanceurs", description=f"**{arme}**", color=0x00ccff, timestamp=datetime.now())
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Spécial", style=discord.ButtonStyle.primary, row=0)
    async def special(self, interaction: discord.Interaction, button: discord.ui.Button):
        armes = find_category_list("Spécial")
        if not armes:
            return await interaction.response.send_message("❌ Aucune arme dans cette catégorie", ephemeral=True)
        arme = random.choice(armes)
        embed = discord.Embed(title="🗡️ PICK 2 — Spécial", description=f"**{arme}**", color=0x00ccff, timestamp=datetime.now())
        await interaction.response.edit_message(embed=embed, view=self)
