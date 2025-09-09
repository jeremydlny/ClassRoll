import discord
from datetime import datetime
from utils.classGenerator import find_category_list
import random

class SecondaireView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)

    @discord.ui.button(label="↩️ Retour", style=discord.ButtonStyle.secondary, row=1)
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

    @discord.ui.button(label='SAUVEGARDER', style=discord.ButtonStyle.success, emoji='💾', row=1)
    async def sauvegarder_arme_secondaire(self, interaction: discord.Interaction, button: discord.ui.Button):
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
                title="💾 Arme Secondaire Sauvegardée",
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

    @discord.ui.button(label="🔫 Pistolets", style=discord.ButtonStyle.primary, row=0)
    async def pistolets(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        armes = find_category_list("Pistolets")
        if not armes:
            return await interaction.followup.send("❌ Aucune arme dans cette catégorie", ephemeral=True)
        
        arme = random.choice(armes)
        embed = discord.Embed(title="🔫 Secondaire — Pistolets", description=f"```{arme}```", color=0x00ccff, timestamp=datetime.now())
        await interaction.edit_original_response(embed=embed, view=self)

    @discord.ui.button(label="🚀 Lanceurs", style=discord.ButtonStyle.primary, row=0)
    async def lanceurs(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        armes = find_category_list("Lanceurs")
        if not armes:
            return await interaction.followup.send("❌ Aucune arme dans cette catégorie", ephemeral=True)
        
        arme = random.choice(armes)
        embed = discord.Embed(title="🔫 Secondaire — Lanceurs", description=f"```{arme}```", color=0x00ccff, timestamp=datetime.now())
        await interaction.edit_original_response(embed=embed, view=self)

    @discord.ui.button(label="⚔️ Spécial", style=discord.ButtonStyle.primary, row=0)
    async def special(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        armes = find_category_list("Spécial")
        if not armes:
            return await interaction.followup.send("❌ Aucune arme dans cette catégorie", ephemeral=True)
        
        arme = random.choice(armes)
        embed = discord.Embed(title="🔫 Secondaire — Spécial", description=f"```{arme}```", color=0x00ccff, timestamp=datetime.now())
        await interaction.edit_original_response(embed=embed, view=self)
