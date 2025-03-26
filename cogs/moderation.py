from discord import app_commands
from discord.ext import commands
import discord

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name = "hello")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello, bienvenue sur le discord Catalyse !", ephemeral=True)

    @app_commands.command(name = "help")
    async def help(self, interaction: discord.Interaction):
        """
        Affiche une liste des commandes disponibles et leur description.
        """
        embed = discord.Embed(
            title="Aide pour Catalyse Lumina",
            description="Bienvenue sur le serveur Discord Catalyse Lumina ! Voici une liste des commandes disponibles :",
            color=0xafeefe,
        )
        embed.add_field(
            name="/hello",
            value="Affiche le guide de bienvenue.",
            inline=False,
        )
        embed.add_field(
            name="/help",
            value="Affiche cette liste des commandes.",
            inline=False,
        )
        embed.add_field(
            name="/regles",
            value="Affiche les règles du serveur",
            inline=False
        )
        embed.add_field(
            name="/sondage",
            value="Crée un sondage avec des options de vote",
            inline=False
        )
        embed.add_field(
            name="Code source du bot",
            value=(
            "Le code source du bot est disponible [ici](https://github.com/Jerenstar/Catalyse-discord-bot.git)."
            ),  
            inline=False,
        )
        await interaction.response.send_message(embed=embed, ephemeral=True) # réponse privée

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} is loaded.")

async def setup(bot):
    await bot.add_cog(ModerationCog(bot))