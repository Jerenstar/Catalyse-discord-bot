import discord
from discord.ext import commands 
from dotenv import load_dotenv
import os

load_dotenv()

class MyBot(commands.Bot):
    async def setup_hook(self):
        for extension in ['moderation', 
                          'press']:
            await self.load_extension(f'cogs.{extension}')


bot = MyBot(command_prefix="!", intents=discord.Intents.all())
@bot.event
async def on_ready():
    await bot.tree.sync()

bot.run(os.getenv('BOT_TOKEN'))
