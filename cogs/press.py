from discord.ext import commands 

class PressCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name = "get_press_resume", aliases = ['press'])
    async def send_press_sumup(self, context, theme:str = "", langue:str = 'francais'):
        authorized_channel = 1354476747306827846
        if context.channel.id != authorized_channel:
            # Autorise a lancer la commande seulement dans le channel commande (evite le spam sur les autres chan)
            # Sinon envoie un message sur le chan ou la commande est lancé visible seulement par le user
            await context.reply("Cette commande est destinée a etre utilisée dans le channel test-commands uniquement ", ephemeral=True)
            return
        user = context.author
        await user.send(f"Hello, voila ce qu'il se passe sur {theme}")
        await context.reply(f"{user.mention}, je vous ai envoyé votre revue de presse sur le theme {theme} !")
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} is loaded.")

async def setup(bot):
    await bot.add_cog(PressCog(bot))