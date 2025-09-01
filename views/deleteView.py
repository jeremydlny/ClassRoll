import discord

class DeleteConfirmView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=30)
        self.bot = bot

    @discord.ui.button(label="🗑️ Oui", style=discord.ButtonStyle.danger)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        count = 0
        async for msg in interaction.channel.history(limit=100):
            if msg.author == self.bot.user:
                try:
                    await msg.delete()
                    count += 1
                except (discord.NotFound, discord.Forbidden):
                    pass
        # Supprimer le message de confirmation
        try:
            await interaction.message.delete()
        except (discord.NotFound, discord.Forbidden):
            pass
        await interaction.followup.send(f"✅ {count} messages du bot supprimés.", ephemeral=True)

    @discord.ui.button(label="❌ Non", style=discord.ButtonStyle.secondary)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("❌ Suppression annulée.", ephemeral=True)
