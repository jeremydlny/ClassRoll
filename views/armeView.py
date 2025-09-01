import discord
from datetime import datetime
from utils.classGenerator import generer_arme_aleatoire, generer_arme_principale, generer_arme_secondaire

class ArmeView(discord.ui.View):
    def __init__(self, classe=None):
        super().__init__(timeout=300)
        self.classe = classe

    @discord.ui.button(label='🔄 ALÉATOIRE', style=discord.ButtonStyle.primary, row=0)
    async def autre_arme(self, interaction: discord.Interaction, button: discord.ui.Button):
        arme = generer_arme_aleatoire()
        embed = discord.Embed(title="🎯 Arme Aléatoire", color=0x0099ff, timestamp=datetime.now())
        embed.add_field(name="🔫 Votre arme", value=f"```{arme}```", inline=False)
        embed.set_footer(text="🍀 Bonne chance !")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label='🔫 PRINCIPALE', style=discord.ButtonStyle.success, row=0)
    async def arme_principale(self, interaction: discord.Interaction, button: discord.ui.Button):
        arme = generer_arme_principale()
        embed = discord.Embed(title="🔫 Arme Principale", color=0x00ff00, timestamp=datetime.now())
        embed.add_field(name="🎯 Votre arme", value=f"```{arme}```", inline=False)
        embed.set_footer(text="🍀 Bonne chance !")
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label='🔫 SECONDAIRE', style=discord.ButtonStyle.success, row=0)
    async def arme_secondaire(self, interaction: discord.Interaction, button: discord.ui.Button):
        arme = generer_arme_secondaire()
        embed = discord.Embed(title="🗡️ Arme Secondaire", color=0xff8800, timestamp=datetime.now())
        embed.add_field(name="🎯 Votre arme", value=f"```{arme}```", inline=False)
        embed.set_footer(text="🍀 Bonne chance !")
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
