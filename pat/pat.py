from discord.ext import commands
import random
import discord

class Pat:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def pat(self, context, member: discord.Member):
        """Pat your senpai/waifu!"""
        author = context.message.author.mention
        mention = member.mention
        
        pat = "**{0} got patted by {1}!**"
        
        choices = ['http://i.imgur.com/10VrpFZ.gif', 'http://i.imgur.com/x0u35IU.gif', 'http://i.imgur.com/0gTbTNR.gif', 'http://i.imgur.com/hlLCiAt.gif', 'http://i.imgur.com/sAANBDj.gif']
        
        image = random.choice(choices)
        
        embed = discord.Embed(description=pat.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Pat(bot)
    bot.add_cog(n)
