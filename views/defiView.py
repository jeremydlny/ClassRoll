import discord
from datetime import datetime
import random
from utils.classGenerator import defis_data, safe_list

class DefiView(discord.ui.View):
    def __init__(self, classe=None):
        super().__init__(timeout=300)
        self.classe = classe

    @discord.ui.button(label='🟢 Facile', style=discord.ButtonStyle.success)
    async def facile(self, interaction: discord.Interaction, button: discord.ui.Button):
        defis_faciles = safe_list(defis_data, 'facile')
        if not defis_faciles:
            await interaction.response.send_message("❌ Aucun défi facile disponible", ephemeral=True)
            return
        defi = random.choice(defis_faciles)
        embed = discord.Embed(title="🟢 Défi Facile", color=0x00ff00, timestamp=datetime.now())
        embed.add_field(name="🎯 Votre défi", value=f"**{defi}**", inline=False)
        embed.set_footer(text="🍀 Relevez le défi !")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label='🟡 Moyen', style=discord.ButtonStyle.primary)
    async def moyen(self, interaction: discord.Interaction, button: discord.ui.Button):
        defis_moyens = safe_list(defis_data, 'moyen')
        if not defis_moyens:
            await interaction.response.send_message("❌ Aucun défi moyen disponible", ephemeral=True)
            return
        defi = random.choice(defis_moyens)
        embed = discord.Embed(title="🟡 Défi Moyen", color=0xffff00, timestamp=datetime.now())
        embed.add_field(name="🎯 Votre défi", value=f"**{defi}**", inline=False)
        embed.set_footer(text="🍀 Relevez le défi !")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label='🔴 Difficile', style=discord.ButtonStyle.danger)
    async def difficile(self, interaction: discord.Interaction, button: discord.ui.Button):
        defis_difficiles = safe_list(defis_data, 'difficile')
        if not defis_difficiles:
            await interaction.response.send_message("❌ Aucun défi difficile disponible", ephemeral=True)
            return
        defi = random.choice(defis_difficiles)
        embed = discord.Embed(title="🔴 Défi Difficile", color=0xff0000, timestamp=datetime.now())
        embed.add_field(name="🎯 Votre défi", value=f"**{defi}**", inline=False)
        embed.set_footer(text="🔥 Bon courage !")
        await interaction.response.edit_message(embed=embed, view=self)
        
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
