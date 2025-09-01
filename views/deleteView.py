import discord
import asyncio

class DeleteConfirmView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=30)
        self.bot = bot

    @discord.ui.button(label="🗑️ Oui", style=discord.ButtonStyle.danger)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        # Récupérer tous les messages du bot en une seule fois (plus efficace)
        messages_to_delete = []
        async for msg in interaction.channel.history(limit=100):
            if msg.author == self.bot.user:
                messages_to_delete.append(msg)
        
        # Supprimer par lots pour être plus efficace
        count = 0
        tasks = []
        
        # Traiter par groupes de 5 messages simultanément
        for i in range(0, len(messages_to_delete), 5):
            batch = messages_to_delete[i:i+5]
            for msg in batch:
                tasks.append(self._delete_message(msg))
            
            # Attendre que le batch soit terminé avant de passer au suivant
            if tasks:
                results = await asyncio.gather(*tasks, return_exceptions=True)
                count += sum(1 for r in results if r is True)
                tasks = []
        
        # Supprimer le message de confirmation
        try:
            await interaction.message.delete()
        except (discord.NotFound, discord.Forbidden):
            pass
            
        await interaction.followup.send(f"✅ {count} messages du bot supprimés.", ephemeral=True)
    
    async def _delete_message(self, message):
        """Helper pour supprimer un message de manière sûre"""
        try:
            await message.delete()
            return True
        except (discord.NotFound, discord.Forbidden):
            return False

    @discord.ui.button(label="❌ Non", style=discord.ButtonStyle.secondary)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("❌ Suppression annulée.", ephemeral=True)
