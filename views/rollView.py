import discord
from datetime import datetime
from utils.classGenerator import generer_classe, generer_arme_aleatoire
from utils.stats import update_stats
from functools import lru_cache

class RollView(discord.ui.View):
    def __init__(self, classe):
        super().__init__(timeout=300)
        self.classe = classe

    @discord.ui.button(label='🔄 RE-ROLL', style=discord.ButtonStyle.primary, row=0)
    async def reroll(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Réponse immédiate pour montrer que le bouton a été cliqué
        await interaction.response.defer()
        
        update_stats("reroll")
        nouvelle_classe = generer_classe()
        self.classe = nouvelle_classe
        embed = create_class_embed(nouvelle_classe)
        
        # Édition après coup pour une meilleure réactivité
        await interaction.edit_original_response(embed=embed, view=self)

    @discord.ui.button(label='🎯 ARME SEULE', style=discord.ButtonStyle.success, row=0)
    async def arme_seule(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Réponse immédiate
        await interaction.response.defer()
        
        # Import local pour éviter les imports circulaires
        from views.armeView import ArmeView
        arme = generer_arme_aleatoire()
        embed = discord.Embed(title="🎯 Arme Aléatoire", color=0x0099ff, timestamp=datetime.now())
        embed.add_field(name="🔫 Votre arme", value=f"```{arme}```", inline=False)
        embed.set_footer(text="🍀 Bonne chance !")
        
        await interaction.edit_original_response(embed=embed, view=ArmeView(self.classe))

    @discord.ui.button(label='🏆 DÉFI', style=discord.ButtonStyle.danger, row=0)
    async def defi(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Réponse immédiate
        await interaction.response.defer()
        
        # Import local pour éviter les imports circulaires
        from views.defiView import DefiView
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
        
        await interaction.edit_original_response(embed=embed, view=view)

    @discord.ui.button(label='🔫 ARME PRINCIPALE', style=discord.ButtonStyle.secondary, row=1)
    async def arme_principale_direct(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        # Import local pour éviter les imports circulaires
        from views.principaleView import PrincipaleView
        update_stats("principale")
        
        view = PrincipaleView()
        embed = discord.Embed(
            title="🔫 Armes principales",
            description="```Choisissez une catégorie pour obtenir une arme aléatoire dedans.```",
            color=0x00ccff,
            timestamp=datetime.now()
        )
        await interaction.edit_original_response(embed=embed, view=view)

    @discord.ui.button(label='🗡️ ARME SECONDAIRE', style=discord.ButtonStyle.secondary, row=1)
    async def arme_secondaire_direct(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        # Import local pour éviter les imports circulaires
        from views.secondaireView import SecondaireView
        update_stats("secondaire")
        
        view = SecondaireView()
        embed = discord.Embed(
            title="🗡️ Armes secondaires",
            description="```Choisissez une catégorie (Pistolets, Lanceurs ou Spécial) pour obtenir une arme aléatoire dedans.```",
            color=0x00ccff,
            timestamp=datetime.now()
        )
        await interaction.edit_original_response(embed=embed, view=view)

    @discord.ui.button(label='SAUVEGARDER', style=discord.ButtonStyle.success, emoji='💾', row=2)
    async def sauvegarder_classe(self, interaction: discord.Interaction, button: discord.ui.Button):
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
            
            # Créer l'embed pour la classe sauvegardée
            embed = discord.Embed(
                title="💾 Classe Sauvegardée",
                description=f"**Sauvegardée par {interaction.user.mention}**",
                color=0x00ff00,
                timestamp=datetime.now()
            )
            embed.add_field(name="🔫 Arme n°1", value=f"```{self.classe['arme_principale']}```", inline=True)
            embed.add_field(name="🔫 Arme n°2", value=f"```{self.classe['arme_secondaire']}```", inline=True)
            embed.add_field(name="", value="", inline=True)  # Spacer
            embed.add_field(name="⚡ Atout 1", value=f"```{self.classe['atout_1']}```", inline=True)
            embed.add_field(name="⚡ Atout 2", value=f"```{self.classe['atout_2']}```", inline=True)
            embed.add_field(name="⚡ Atout 3", value=f"```{self.classe['atout_3']}```", inline=True)
            embed.add_field(name="🎯 Équipement tactique", value=f"```{self.classe['equipement_tactique']}```", inline=True)
            embed.add_field(name="💥 Équipement mortel", value=f"```{self.classe['equipement_mortel']}```", inline=True)
            embed.add_field(name="", value="", inline=True)  # Spacer
            embed.set_footer(text=f"Sauvegardée depuis #{interaction.channel.name}")
            
            # Envoyer la classe dans le salon "classe"
            await salon_classe.send(embed=embed)
            
        except Exception as e:
            await interaction.followup.send(
                f"❌ **Erreur lors de la sauvegarde :** {str(e)}",
                ephemeral=True
            )

@lru_cache(maxsize=128)  # Cache pour éviter de recréer les mêmes embeds
def _create_embed_cached(arme_principale, arme_secondaire, atout_1, atout_2, atout_3, equipement_tactique, equipement_mortel, timestamp_str):
    """Version cachée de create_class_embed pour de meilleures performances"""
    embed = discord.Embed(title="🎲 Classe Générée", color=0x0099ff, timestamp=datetime.fromisoformat(timestamp_str))
    embed.add_field(name="🔫 Arme n°1", value=f"```{arme_principale}```", inline=True)
    embed.add_field(name="🔫 Arme n°2", value=f"```{arme_secondaire}```", inline=True)
    embed.add_field(name="", value="", inline=True)  # Spacer
    embed.add_field(name="⚡ Atout 1", value=f"```{atout_1}```", inline=True)
    embed.add_field(name="⚡ Atout 2", value=f"```{atout_2}```", inline=True)
    embed.add_field(name="⚡ Atout 3", value=f"```{atout_3}```", inline=True)
    embed.add_field(name="🎯 Équipement tactique", value=f"```{equipement_tactique}```", inline=True)
    embed.add_field(name="💥 Équipement mortel", value=f"```{equipement_mortel}```", inline=True)
    embed.add_field(name="", value="", inline=True)  # Spacer
    embed.set_footer(text="🍀 Bonne chance!")
    return embed

def create_class_embed(classe):
    """Créer un embed Discord pour afficher la classe générée (version optimisée)"""
    # Utiliser la version cachée avec un timestamp arrondi à la seconde pour améliorer le cache hit rate
    timestamp_str = datetime.now().replace(microsecond=0).isoformat()
    
    return _create_embed_cached(
        classe['arme_principale'],
        classe['arme_secondaire'], 
        classe['atout_1'],
        classe['atout_2'],
        classe['atout_3'],
        classe['equipement_tactique'],
        classe['equipement_mortel'],
        timestamp_str
    )
