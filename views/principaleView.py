import discord
from datetime import datetime
from utils.classGenerator import find_category_list
import random

class PrincipaleView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)

    @discord.ui.button(label="🔫 Fusils d'assaut", style=discord.ButtonStyle.primary, row=0)
    async def fusils_assaut(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Réponse immédiate pour la réactivité
        await interaction.response.defer()
        
        armes = find_category_list("Fusils d'assaut")
        if not armes:
            return await interaction.followup.send("❌ Aucune arme dans cette catégorie", ephemeral=True)
        
        arme = random.choice(armes)
        embed = discord.Embed(title="🔫 Principale — Fusils d'assaut", description=f"```{arme}```", color=0x00ccff, timestamp=datetime.now())
        await interaction.edit_original_response(embed=embed, view=self)

    @discord.ui.button(label="🔫 Mitraillettes", style=discord.ButtonStyle.primary, row=0)
    async def mitraillettes(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        armes = find_category_list("Mitraillettes")
        if not armes:
            return await interaction.followup.send("❌ Aucune arme dans cette catégorie", ephemeral=True)
        
        arme = random.choice(armes)
        embed = discord.Embed(title="🔫 Principale — Mitraillettes", description=f"```{arme}```", color=0x00ccff, timestamp=datetime.now())
        await interaction.edit_original_response(embed=embed, view=self)

    @discord.ui.button(label="🔫 Fusils à pompe", style=discord.ButtonStyle.primary, row=1)
    async def fusils_pompe(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        armes = find_category_list("Fusils à pompe")
        if not armes:
            return await interaction.followup.send("❌ Aucune arme dans cette catégorie", ephemeral=True)
        
        arme = random.choice(armes)
        embed = discord.Embed(title="🔫 Principale — Fusils à pompe", description=f"```{arme}```", color=0x00ccff, timestamp=datetime.now())
        await interaction.edit_original_response(embed=embed, view=self)

    @discord.ui.button(label="🔫 Mitrailleuses", style=discord.ButtonStyle.primary, row=1)
    async def mitrailleuses(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        armes = find_category_list("Mitrailleuses")
        if not armes:
            return await interaction.followup.send("❌ Aucune arme dans cette catégorie", ephemeral=True)
        
        arme = random.choice(armes)
        embed = discord.Embed(title="🔫 Principale — Mitrailleuses", description=f"```{arme}```", color=0x00ccff, timestamp=datetime.now())
        await interaction.edit_original_response(embed=embed, view=self)

    @discord.ui.button(label="🔫 Fusils tactiques", style=discord.ButtonStyle.primary, row=2)
    async def fusils_tactiques(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        armes = find_category_list("Fusils tactiques")
        if not armes:
            return await interaction.followup.send("❌ Aucune arme dans cette catégorie", ephemeral=True)
        
        arme = random.choice(armes)
        embed = discord.Embed(title="🔫 Principale — Fusils tactiques", description=f"```{arme}```", color=0x00ccff, timestamp=datetime.now())
        await interaction.edit_original_response(embed=embed, view=self)

    @discord.ui.button(label="🔫 Fusils de précision", style=discord.ButtonStyle.primary, row=2)
    async def fusils_precision(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        armes = find_category_list("Fusils de précision")
        if not armes:
            return await interaction.followup.send("❌ Aucune arme dans cette catégorie", ephemeral=True)
        
        arme = random.choice(armes)
        embed = discord.Embed(title="🔫 Principale — Fusils de précision", description=f"```{arme}```", color=0x00ccff, timestamp=datetime.now())
        await interaction.edit_original_response(embed=embed, view=self)

    @discord.ui.button(label="↩️ Retour", style=discord.ButtonStyle.secondary, row=3)
    async def retour(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Réponse immédiate
        await interaction.response.defer()
        
        # Import local pour éviter les imports circulaires
        from views.rollView import RollView, create_class_embed
        from utils.classGenerator import generer_classe
        classe = generer_classe()
        embed = create_class_embed(classe)
        view = RollView(classe)
        await interaction.edit_original_response(embed=embed, view=view)

    @discord.ui.button(label='SAUVEGARDER', style=discord.ButtonStyle.success, emoji='💾', row=3)
    async def sauvegarder_arme_principale(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        
        try:
            # Trouver le salon "classe" dans le serveur
            salon_classe = None
            for channel in interaction.guild.text_channels:
                if channel.name == "🔫・classe":
                    salon_classe = channel
                    break
            
            if not salon_classe:
                return await interaction.followup.send(
                    "❌ **Salon '🔫・classe' introuvable** - Assurez-vous qu'un salon textuel nommé '🔫・classe' existe sur ce serveur.",
                    ephemeral=True
                )
            
            # Récupérer l'arme depuis l'embed actuel
            embed_actuel = interaction.message.embeds[0]
            arme = embed_actuel.description.strip('```')
            titre_arme = embed_actuel.title
            
            # Créer l'embed pour l'arme sauvegardée
            embed = discord.Embed(
                title="💾 Arme Principale Sauvegardée",
                description=f"**Sauvegardée par {interaction.user.mention}**",
                color=0x00ff00,
                timestamp=datetime.now()
            )
            embed.add_field(name=titre_arme, value=f"```{arme}```", inline=False)
            embed.set_footer(text=f"Sauvegardée depuis #{interaction.channel.name}")
            
            # Envoyer l'arme dans le salon "classe"
            await salon_classe.send(embed=embed)
            
        except Exception as e:
            await interaction.followup.send(
                f"❌ **Erreur lors de la sauvegarde :** {str(e)}",
                ephemeral=True
            )
