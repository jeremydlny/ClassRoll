import discord
from datetime import datetime
from utils.classGenerator import generer_arme_aleatoire, generer_arme_principale, generer_arme_secondaire

class ArmeView(discord.ui.View):
    def __init__(self, classe=None):
        super().__init__(timeout=300)
        self.classe = classe

    @discord.ui.button(label='🔄 RE-ROLL', style=discord.ButtonStyle.success, row=0)
    async def autre_arme(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        arme = generer_arme_aleatoire()
        embed = discord.Embed(title="🎯 Arme Aléatoire", color=0x0099ff, timestamp=datetime.now())
        embed.add_field(name="🔫 Votre arme", value=f"```{arme}```", inline=True)
        embed.set_footer(text="🍀 Bonne chance !")
        await interaction.edit_original_response(embed=embed, view=self)

    @discord.ui.button(label='↩️ RETOUR', style=discord.ButtonStyle.secondary, row=0)
    async def retour(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        from views.rollView import RollView, create_class_embed
        if self.classe:
            view = RollView(self.classe)
            embed = create_class_embed(self.classe)
            await interaction.edit_original_response(embed=embed, view=view)
        else:
            # Si pas de classe sauvegardée, en générer une nouvelle
            from utils.classGenerator import generer_classe
            nouvelle_classe = generer_classe()
            view = RollView(nouvelle_classe)
            embed = create_class_embed(nouvelle_classe)
            await interaction.edit_original_response(embed=embed, view=view)

    @discord.ui.button(label='SAUVEGARDER', style=discord.ButtonStyle.success, emoji='💾', row=1)
    async def sauvegarder_arme(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        
        try:
            # Trouver le salon "classe" dans le serveur
            salon_classe = None
            for channel in interaction.guild.text_channels:
                if channel.name.lower() == "classe":
                    salon_classe = channel
                    break
            
            if not salon_classe:
                return await interaction.followup.send(
                    "❌ **Salon 'classe' introuvable** - Assurez-vous qu'un salon textuel nommé 'classe' existe sur ce serveur.",
                    ephemeral=True
                )
            
            # Récupérer l'arme depuis l'embed actuel
            embed_actuel = interaction.message.embeds[0]
            arme = embed_actuel.fields[0].value.strip('```')
            
            # Créer l'embed pour l'arme sauvegardée
            embed = discord.Embed(
                title="💾 Arme Sauvegardée",
                description=f"**Sauvegardée par {interaction.user.mention}**",
                color=0x00ff00,
                timestamp=datetime.now()
            )
            embed.add_field(name="🔫 Arme aléatoire", value=f"```{arme}```", inline=False)
            embed.set_footer(text=f"Sauvegardée depuis #{interaction.channel.name}")
            
            # Envoyer l'arme dans le salon "classe"
            await salon_classe.send(embed=embed)
            
        except Exception as e:
            await interaction.followup.send(
                f"❌ **Erreur lors de la sauvegarde :** {str(e)}",
                ephemeral=True
            )
